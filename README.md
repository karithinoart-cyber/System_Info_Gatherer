# 🖥️ System Information Gatherer

A professional Python-based system information gathering tool that collects detailed information about a computer and generates comprehensive reports in multiple formats.

---

## 📌 Overview

System Information Gatherer is a cross-platform Python application that collects hardware, software, network, process, and user information from the local system. It generates structured reports that can be used for system inventory, auditing, troubleshooting, and learning about system administration.

> **Note:** This project is intended for collecting information from systems that you own or are authorized to inspect.

---

## ✨ Features

### 🖥️ System Information

* Operating System
* System Architecture
* Hostname
* Python Version
* Boot Time
* System Uptime

### ⚙️ Hardware Information

* CPU Information
* RAM Information
* Disk Information
* Battery Information
* Motherboard Information (Windows)

### 🌐 Network Information

* Hostname
* Private IP Address
* Public IP Address
* MAC Address
* Network Interfaces
* Network Statistics
* Active Connections

### 📦 Software Information

* Installed Software
* Installed Python Packages
* Python Runtime Information

### 👤 User Information

* Current User
* Logged-in Users
* Administrator Detection
* Environment Variables
* User Sessions

### 📊 Process Information

* Running Processes
* Top CPU Usage
* Top Memory Usage
* Process Summary

### 📄 Report Generation

* JSON Report
* TXT Report
* HTML Report

### 🔐 Integrity Verification

* SHA-256 Hash
* SHA-1 Hash
* MD5 Hash

### 📝 Logging

* Console Logging
* Log File Generation

---

# 📂 Project Structure

```text
System_Info_Gatherer/
│
├── main.py
├── config.py
├── banner.py
├── logger.py
├── utils.py
├── system_info.py
├── hardware_info.py
├── network_info.py
├── process_info.py
├── software_info.py
├── user_info.py
├── hash_generator.py
├── report_generator.py
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── reports/
├── logs/
└── screenshots/
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/karithinoart-cyber/System-Info-Gatherer.git
```

Navigate to the project directory:

```bash
cd System-Info-Gatherer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Run the application:

```bash
python main.py
```

---

# 📁 Generated Reports

The application automatically creates reports inside the `reports` folder.

Example:

```
reports/
│
├── System_Report_20260704_182500.json
├── System_Report_20260704_182500.txt
└── System_Report_20260704_182500.html
```

---

# 🛠 Technologies Used

* Python 3
* psutil
* requests
* colorama
* hashlib
* pathlib
* json

---

# 📋 Sample Output

```
==============================
System Information Gatherer
==============================

Operating System : Windows 11
Processor        : Intel Core i7
RAM              : 16 GB
Private IP       : 192.168.1.100
Public IP        : xxx.xxx.xxx.xxx

Reports Generated Successfully
```

---

# 🚀 Future Improvements

* PDF Report Generation
* CSV Export
* GPU Information
* USB Device Information
* Installed Drivers
* Browser Information
* Scheduled Tasks
* Wi-Fi Information
* Command-Line Options
* Unit Tests
* GitHub Actions (CI)

---

# 🤝 Contributing

Contributions, bug reports, feature requests, and improvements are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
