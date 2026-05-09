# Phase 2: Offensive Scripting & Reconnaissance Toolkit 🛡️

**University:** UOP (Faculty of Information Technology)  
**Course:** Information And Network Security Programming (605346)  
**Academic Year:** 2025 – 2026, Semester 2  

## 📖 Overview
This repository contains Phase 2 of our Network Security Project. It extends our Phase 1 multithreaded port scanner by introducing an automated reconnaissance module, an SSH interaction module, and an educational, sandboxed reverse shell payload. 

This toolkit was built strictly for authorized lab environments to demonstrate offensive scripting concepts and their respective mitigation strategies.

## ⚠️ Ethical Use Policy
**IMPORTANT:** This toolkit is developed *exclusively* for educational purposes. All tools and payloads within this repository are hardcoded to target local/loopback addresses (e.g., `127.0.0.1`, `localhost`). Testing these scripts against unauthorized external systems is strictly prohibited and violates the UOP Academic Honesty Policy. 

## ⚙️ Prerequisites
To run these tools, you need Python 3.x installed along with the following external libraries:
```bash
pip install paramiko dnspython python-whois
