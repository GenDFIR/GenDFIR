## 🤖 GenDFIR 🤖

This repository contains the case studies from the paper: *"GenDFIR: Advancing Cyber Incident Timeline Analysis Through Retrieval-Augmented Generation and Large Language Models."* 

The cyber incident scenarios are synthetic, designed and rigorously evaluated to replicate real-life incidents while adhering to privacy, constraint, and confidentiality concerns.

## 6 Different Cyber Incident Scenarios ##
1- DNS-SPOOF: This incident involves a DNS spoofing scenario where multiple event logs were collected from various devices, including Windows event logs, DNS server logs, firewall records, and network traffic monitoring tools. Irregularities such as delayed DNS responses, inconsistent resolutions, and unexpected outbound traffic were identified, triggering alerts from the Intrusion Detection System (IDS) and performance monitoring tools.
  • Each event log represents a chunk.
2- Phishing Email 1: This scenario represents a phishing attack where an employee was targeted by emails impersonating a security service. The organisation’s policy prohibits communication with untrusted domains, permitting only interactions with verified sources. All suspicious emails were collected for analysis, focusing on domains, sender and receiver details, IP addresses, email content, and timestamps to determine the nature of the attack.
  • Each single Email represents a chunk.
3- Phishing Email 2: Same as the previous scenario, this is a phishing attack where an employee was targeted by emails impersonating a trusted support service, attempting to deceive the employee into verifying account information. The organisation’s policy restricts communication with unverified domains and permits only trusted sources. All suspicious emails received during the suspected phishing period were collected for analysis, focusing on domains, sender and receiver details, IP addresses, email content, and timestamps to assess the nature of the attack.
  • Each single Email represents a chunk
4- Rhino Hunt: This scenario is inspired by the well-known "Rhino Hunt" incident, but in this case, it involves the illegal exfiltration of copyrighted rhino images. An unauthorised individual accessed the company’s FTP server and stole twelve protected images. The investigation traced the exfiltration to a device within the company’s internal network, with the stolen data directed to an external IP address. Forensic analysis revealed that the user associated with the IP address possessed additional images matching the stolen ones. The collected data included images that met specific metadata criteria, including camera model, artist, and copyright details.
    - The images used in this scenario are AI-generated (using DALL·E 3) for the purpose of ensuring copyright compliance and consent. The metadata of the images has been modified to align with the scenario description and can be extracted and viewed using the Metaminer module.
  • The events in this scenario represent log entries where the context of the image has been added at the beginning of each event to enrich the entry with additional context.
5- SYN FLOOD: This is a SYN flood attack, where unusual network events disrupted standard operations. The anomalies were characterised by a high volume of Synchronise (SYN) requests, causing intermittent service degradation across the network. Data was collected from firewalls, network scanners, and Intrusion Detection Systems (IDS). The analysis focus on critical attributes such as event ID, details, level, timestamps, source, task category, and affected devices to assess the nature of the attack and identify potential threats or operational issues.
  • Each event log represents a chunk.
6- Unauthorised Access: This scenario is an unauthorised access attempt detected by an intrusion detection system (IDS). The system flagged multiple access attempts from a blacklisted IP address, which was not authorised for any legitimate activity within the network. The collected data, including warnings, errors, and critical alerts, provided the basis for further investigation into the potential breach.
  • Each event log represents a chunk.

### Each scenario includes:
- A description of the Incident.
- A knowledge base containing all incident events.
- 40 evaluation metric prompts for each scenario, with 20 prompts dedicated to each metric, including answers and their corresponding judgments (false or correct). Across all scenarios, this results in a total of 240 DFIR prompts.
- GenDFIR Timeline Analysis Reports for each scenario.
- Incorrect Facts (Noise) in the GenDFIR auto-generated Timeline Analysis Reports for each scenario (detected after the assessment of the report related to the Accuracy metric).
