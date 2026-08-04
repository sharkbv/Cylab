"""
CYLAB Pipeline
Runs scan -> webscan -> exploit lookup automatically, saving each result.
"""

import re

from cylab.core.scanner import run_scan
from cylab.core.webscan import run_nikto, run_gobuster
from cylab.core.nuclei import run_nuclei
from cylab.core.exploitdb import search_exploits
from cylab.core.metasploit import search_modules
from cylab.core.scanstore import save_result


def extract_services(nmap_output):
    services = []
    if not nmap_output:
        return services
    for line in nmap_output.splitlines():
        m = re.match(r"^\d+/tcp\s+open\s+(\S+)\s+(.+)$", line.strip())
        if m:
            product_version = m.group(2).strip()
            if product_version:
                services.append(product_version)
    return services


def has_web_port(nmap_output):
    if not nmap_output:
        return False
    return bool(re.search(r"^(80|443|8080|8000)/tcp\s+open", nmap_output, re.MULTILINE))


def run_assessment(target, web_url=None):
    log = []

    log.append(f"[1/4] Scanning {target} with Nmap...")
    nmap_out = run_scan(target, profile="quick")
    if nmap_out in (None, "TIMEOUT"):
        log.append("Nmap scan failed or timed out.")
        return "\n".join(log)
    save_result(target, "nmap", nmap_out)
    log.append(nmap_out)

    services = extract_services(nmap_out)

    if web_url or has_web_port(nmap_out):
        url = web_url or f"http://{target}"
        log.append(f"\n[2/4] Web scan on {url}...")
        gobuster_out = run_gobuster(url)
        if gobuster_out and gobuster_out != "TIMEOUT":
            save_result(target, "webscan", gobuster_out)
            log.append(gobuster_out)

        nuclei_out = run_nuclei(url)
        if nuclei_out and nuclei_out != "TIMEOUT":
            save_result(target, "nuclei", nuclei_out)
            log.append(f"\n[Nuclei results]\n{nuclei_out}")
    else:
        log.append("\n[2/4] No web port detected, skipping web scan.")

    if services:
        log.append(f"\n[3/4] Searching known exploits for {len(services)} service(s)...")
        combined_sploit = []
        combined_msf = []
        for svc in services:
            r1 = search_exploits(svc)
            if r1:
                combined_sploit.append(f"-- {svc} --\n{r1}")
            r2 = search_modules(svc)
            if r2 and r2 != "TIMEOUT":
                combined_msf.append(f"-- {svc} --\n{r2}")
        if combined_sploit:
            save_result(target, "searchsploit", "\n\n".join(combined_sploit))
        if combined_msf:
            save_result(target, "msf", "\n\n".join(combined_msf))
        log.append("Done searching exploits.")
    else:
        log.append("\n[3/4] No service versions detected, skipping exploit search.")

    log.append("\n[4/4] Assessment complete. Run 'cylab agent advise' for AI analysis.")
    return "\n".join(log)
