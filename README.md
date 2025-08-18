# Vodafone GigaCube Rebooter

Automatically monitor your Vodafone GigaCube router and reboot it when internet connectivity is lost.

---

## Why This Tool Exists

For the past 3 weeks, Vodafone has been experiencing issues with their signal tower. As a result, I frequently have no internet for long periods of time, and the only workaround is to manually reboot the GigaCube router. After rebooting, I may get a connection for a few minutes to a few hours, and then the same problem repeats.  

This tool automates that process, keeping the internet connected without constant manual intervention.

---

## Features

- Periodically checks internet connectivity using multiple test URLs.
- Automatically logs in to your Vodafone GigaCube router using a local Brave browser.
- Navigates the router’s web interface to restart it when internet is down.
- Fully offline capable using a local ChromeDriver bundled with Brave.
- Minimal setup and configurable wait times.

---

## Requirements

- Python 3.10+
- Brave Browser installed
- Chromedriver matching Brave version
- Python packages (listed in `requirements.txt`)
- `.env` file containing your router password:

```env
ROUTER_PASSWORD=yourpasswordhere
```

**Note:** Brave and Chromedriver paths depend on your installed browser and version. The paths and versions used in this repository are for personal preference and may need to be updated for your system.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/RamezCh/Vodafone_GigaCube_Rebooter.git
cd Vodafone_GigaCube_Rebooter
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your router password:

```env
ROUTER_PASSWORD=yourpasswordhere
```

4. Update paths to Brave and Chromedriver in the script if necessary:

```python
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
CHROMEDRIVER_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\139.1.81.135\chromedriver.exe"
```

---

## Usage

Run the script:

```bash
python vodafone_gigacube_rebooter.py
```

The script will:

1. Check internet connectivity.
2. If down, open Brave and log in to your Vodafone GigaCube router.
3. Navigate to Advanced Settings → Others → Restart.
4. Wait for the router to reboot, then check connectivity again.
5. Repeat until internet is restored.

---

## Configuration

- INTERNET_TEST_URLS: List of URLs used to test connectivity.
- REBOOT_WAIT: Seconds to wait after restarting router before rechecking internet.
- TIMEOUT: Timeout for waiting on router page elements.

All configuration values can be updated at the top of the Python script.

---

## Notes

- This tool is designed for Vodafone GigaCube routers specifically.
- You can run it offline; it uses local Brave + Chromedriver.
- Brave and Chromedriver paths may vary depending on your installation and version.

---

## Disclaimer

Use this script responsibly. It is intended for personal use with your own Vodafone router. Frequent restarts may interfere with other network users or violate Vodafone terms of service.

---

## License

MIT License
