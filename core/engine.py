from modules import port_scan, banner_grab
from detection.analyzer import analyze_results
from utils.logger import setup_logger
from utils.report import save_report

class Scanner:
    def __init__ (self, target):
        self.target = target
        self.logger = setup_logger()
        self.results = {}
    def run(self):
        self.logger.info(f"Starting scan on {self.target}")
        self.results['ports'] = port_scan.scan(self.target)
        self.results['banners'] = banner_grab.grab(self.target, self.results['ports'])

        analyze_results(self.results)
        save_report(self.results)

        self.logger.info("Scan complete")
