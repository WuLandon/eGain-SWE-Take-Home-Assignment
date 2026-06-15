# Package Tracker Chatbot Prototype

A command-line customer service chatbot that helps users track lost packages.

This project demonstrates a chatbot conversation flow for helping a customer track a lost package.

---

## Overview

The chatbot helps customers track missing packages through a guided customer service workflow. Users can:

- Check the status of a package using a tracking number
- Receive shipment updates for packages that are in transit or delayed
- Get help locating a tracking number
- Initiate a missing package claim for delivered packages
- Recover from invalid or unexpected inputs through error handling

---

## Approach

The chatbot was designed around a [decision-tree](#conversation-flowchart) conversation flow that helps users navigate package tracking and delivery issues in a clear and intuitive way.

### Key Conversation Paths

- User has a tracking number
- User needs help finding a tracking number
- Package is in transit
- Package is delayed
- Package has been delivered
- Missing package claim creation

### Error Handling

The chatbot handles several unexpected input scenarios, including:

- Invalid tracking number format
- Tracking number not found
- Invalid responses to yes/no questions

This ensures the user can recover from mistakes or receive additional guidance to continue the conversation successfully.

---

## Conversation Flowchart

![Conversation Flow](/docs/flowchart.png)

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd eGain-SWE-Take-Home-Assignment
```

### Run the Chatbot

```bash
python3 chatbot.py
```

No external dependencies are required.

---

## Demo

The following recording demonstrates:

1. Helping a user locate their tracking number
2. Handling an invalid tracking number entry
3. Handling a tracking number that is not found in the system
4. Viewing delivery status and package details
5. Creating a missing package claim for a delivered package

![Package Tracker Demo](/demos/demo.gif)

---

## Demo Conversation

```text
Welcome to Package Tracker!
I can help you track a missing package.

Do you have your tracking number? (yes/no): no

You can usually find your tracking number in:
- Your shipping confirmation email
- Your order confirmation page
- Your carrier's mobile app

Were you able to locate your tracking number? (yes/no): yes
Please enter your tracking number (e.g., 12345): abc

Invalid tracking number.
Please enter a valid 5-digit tracking number (e.g., 12345): 22222

Tracking number not found.
Please check your tracking number and try again: 34567

Tracking Status: Delivered
Tracking shows your package was delivered on June 13, 2026.
I can help start a missing package investigation.

Would you like to open a missing package claim? (yes/no): yes

Missing package claim created.
A support specialist will follow up with you shortly.

Thank you for using Package Tracker. Goodbye!
```

---

## Project Structure

```text
package-tracker-chatbot/
│
├── chatbot.py
├── README.md
│
├── demos/
│   ├── demo.gif
│   └── demo.tape
│
├── docs/
│   └── flowchart.png
│
└── package_tracker/
    ├── conversation_handlers.py
    ├── messages.py
    ├── tracking_data.py
    └── user_input.py
```

---

## Technologies Used

- Python 3
- Command-Line Interface (CLI)
- Decision Tree Conversation Design

---
