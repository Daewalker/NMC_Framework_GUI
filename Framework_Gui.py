from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo

window = Tk()

window.title("NMC Assistance Framework Application")
window.geometry('800x350')

def clear():
    combo.set('')

def generate_email_template(ticket_num, team_name, device_name, alarm_description):
    email_subject = f"{ticket_num} - {device_name} - {alarm_description}"
    email_body = (
        f"Hello {team_name},\n\n"
        f"This email is to provide visibility on {device_name}, which is currently alarming within SL1."
        f" Alarm: {alarm_description}. \n\n\n"
        f"Please, when possible, could we investigate this issue and reply back to this email chain for visibility into this event.\n"
        f"Thank you.\n\n"
        f"Regards,\n\n"
    )
    
    email_template_window = Toplevel(window)
    email_template_window.title("Generated Email Template")
    email_template_window.geometry('600x400')

    Label(email_template_window, text="Email Subject:", font=('Helvetica 12 bold')).pack(anchor=W, padx=10, pady=5)
    subject_text = Text(email_template_window, height=2, wrap=WORD)
    subject_text.pack(padx=10, pady=5, fill=BOTH)
    subject_text.insert(END, email_subject)
    subject_text.config(state=DISABLED)

    Label(email_template_window, text="Email Body:", font=('Helvetica 12 bold')).pack(anchor=W, padx=10, pady=5)
    body_text = Text(email_template_window, wrap=WORD)
    body_text.pack(padx=10, pady=5, fill=BOTH, expand=True)
    body_text.insert(END, email_body)
    body_text.config(state=DISABLED)

    Button(email_template_window, text="Close", command=email_template_window.destroy).pack(pady=10)

def generate_event_template(event_type, start_date, start_time, end_date, end_time, service_type, cust_affected, sites_affected, alerts, summary, root_cause, sw_vers):
    try:
        start_time = int(start_time)
        end_time = int(end_time)
        
        start_hour = start_time // 100
        start_minute = start_time % 100
        end_hour = end_time // 100
        end_minute = end_time % 100

        start_minutes = start_hour * 60 + start_minute
        end_minutes = end_hour * 60 + end_minute
        total_duration_minutes = end_minutes - start_minutes

        total_duration_hours = total_duration_minutes // 60
        total_duration_minutes %= 60

        event_body = (
            f"  Event Type: {event_type},\n"
            f"  Event Duration: {start_date} @ ({start_time}) - {end_date} @ ({end_time}), Duration: [{total_duration_hours}H:{total_duration_minutes}M] \n"
            f"  Type of Service: {service_type} \n"
            f"  Customers Affected: {cust_affected} \n"
            f"  Numbers of sites: {sites_affected} \n"
            f"  Alerts: {alerts} \n"
            f"  Event Summary: {summary} \n"
            f"  Root Cause: {root_cause} \n"
            f"  S/W Version: {sw_vers} \n"
        )

        event_template_window = Toplevel(window)
        event_template_window.title("Generated Event Template")
        event_template_window.geometry('600x400')

        Label(event_template_window, text="Event Summary Template", font=('Helvetica 12 bold')).pack(anchor=W, padx=10, pady=5)
        event_text = Text(event_template_window, wrap=WORD)
        event_text.pack(padx=10, pady=5, fill=BOTH, expand=True)
        event_text.insert(END, event_body)
        event_text.config(state=DISABLED)

        Button(event_template_window, text="Close", command=event_template_window.destroy).pack(pady=10)

    except ValueError:
        showinfo('Error', 'Please enter valid numeric values for start time and end time.')

def show_submenu(selected_choice):
    submenu_window = Toplevel(window)
    submenu_window.title("Submenu Selection")
    submenu_window.geometry('400x600')

    Label(submenu_window, text=f'Your choice is {selected_choice}', font=('Helvetica 12')).pack(pady=10)
    
    instructions = {
        'Phone Calls': 'Please follow the protocol for handling phone calls.',
        'J1/2 Issues': 'Refer to the J1/2 troubleshooting guide.',
        'J3/FUSION': 'Check the FUSION manual for detailed steps.',
        'Ku Issues': 'Ensure all connections are secure and refer to the Ku band manual.',
        'Email Template': 'Use the provided email templates for communication.',
        'IGT/XCI Issues': 'Follow the IGT/XCI troubleshooting steps.',
        'Escalation Pathes': 'Refer to the escalation path documentation.',
        'Tool Login info': 'Ensure you have the latest login credentials.',
        'Event Summary': 'Summarize the event in the provided format.',
        'Site Access Requests': 'Submit site access requests using the official form.'
    }
    
    instruction = instructions.get(selected_choice, "No instructions available for this selection.")
    
    Label(submenu_window, text=f'Instructions:\n{instruction}', font=('Helvetica 12')).pack(pady=10)

    submenu_options_dict = {
        'Phone Calls': ['Answer Script', 'What do I gather from calls?', 'Transferring Calls'],
        'J1/2 Issues': ['Single sites', 'Terminal drops', 'BGP Peering', 'Move Allows'],
        'J3/FUSION': ['J3_Single sites', 'J3_Terminal drops', 'J3_BGP Peering', 'J3_Move Allows'],
        'Ku Issues': ['Enterprise', 'Timing/Power', 'VSAT Outages/Down', 'Decommission Requests', 'CAC Key Upload'],
        'Email Template': ['Compose New'],
        'IGT/XCI Issues': ['IGT DHCP Pool Purge', 'IGT site not downloading', 'XCI Issues'],
        'Escalation Pathes': ['SDG', 'CNE-GW', 'CNE-NMS', 'NI', 'ESE [ENOC]', 'EDSE', 'HNSec', 'HNSoc'],
        'Tool Login info': ['Jupiter 1 & 2', 'Ku & Terrestrial', 'Jupiter 3'],
        'Event Summary': ['Compose Event Summary'],
        'Site Access Requests': ['SA_Template']
    }

    submenu_options = submenu_options_dict.get(selected_choice, [])

    selected_submenu = StringVar()
    if submenu_options:
        selected_submenu.set(submenu_options[0])
    
    for option in submenu_options:
        Radiobutton(submenu_window, text=option, variable=selected_submenu, value=option).pack(anchor=W, padx=20)

    templates = {
        'Email Template': ['Salesforce Case Number', 'Team to Escalate To', 'Device Name', 'Alarm Description'],
        'Event Summary': ['Event Type', 'Event Start DATE', 'Event Start TIME (24hr)', 'Event End DATE', 'Event End TIME (24hr)', 'Service Type', 'Customers Affected', 'Number of Sites Affected', 'Alert Method', 'Event Summary', 'Root Cause', 'Software Version']
    }

    input_fields = {}
    for template, fields in templates.items():
        if selected_choice == template:
            Label(submenu_window, text=f'{template} Inputs:', font=('Helvetica 12')).pack(pady=5)
            input_fields[template] = []
            for field in fields:
                Label(submenu_window, text=field).pack(padx=20, anchor=W)
                entry = Entry(submenu_window)
                entry.pack(padx=20, pady=5, anchor=W)
                input_fields[template].append(entry)

    Button(submenu_window, text="Submit", command=lambda: submit_submenu(selected_submenu.get(), submenu_window, selected_choice, input_fields)).pack(pady=10)

def submit_submenu(selected_option, submenu_window, main_choice, input_fields):
    procedures_dict = {
        'Answer Script': 'Hello and thank you for calling Hughes NMC, This is <Your Name> speaking, how can I assist you today?',
        'What do I gather from calls?': 'Gather the caller\'s NAME, Where they are calling from, What is the issue?, Site SAN/Serial/Platform/State Codes.',
        'Transferring Calls': 'Transferring is as simple as entering "88" followed by the 4 digit extension of the person you are transferring to. [ex: 883317]',
        'Single sites': "The site SAN, and the SERIAL numbers of the terminal(s) -> There may be more than one - Log into DSS (hns-username:PIN+RSA) and navigate the sidebar to 'Jupiter Dashboard' - Select 'Jupiter Dashboard', then enter the SAN or the ESN of the site into DSS to gather more information, - such as, Radio_ESN, Gateway_IDs, Beam_IDs, etc.",
        'Terminal drops': "Check the site 'uptime', 'downtime', and 'avg packets dropped' - Ensure to look at the Ethernet stats and the last 24 hours - Review these with the customer, escalate to CNE-NMS, CNE-GW, or SDG_Support teams as needed - Have you referenced the 'Hughes Performance Metrics' sheet yet?",
        'BGP Peering': 'Reference the BGP Peering guide for troubleshooting steps.',
        'Move Allows': 'Follow the Move Allows process documented in the NMC procedures.',
        'J3_Single sites': 'Check the J3 Single Site Troubleshooting documentation.',
        'J3_Terminal drops': 'Follow the J3 Terminal Drops troubleshooting guide.',
        'J3_BGP Peering': 'Use the J3 BGP Peering procedures for guidance.',
        'J3_Move Allows': 'Refer to the J3 Move Allows protocol.',
        'Enterprise': 'Log into the Enterprise Vision box via NOC_Forms, - Enter the site SAN and ensure it is correct, - Within the Enterprise Tab look for the site Serial number, - Click on the Serial Number, the IP address within the configuration tab and verify if the site is online, - Is the site offline? Ensure the site is powered on, - Verify there are no weather related events affecting the terminal, - If the terminal is online, verify packet loss and reachability.',
        'Timing/Power': "Gather the SID and Serial numbers of the terminal that is to be decommissioned., - Log into the corresponding Vision box via NOC_Forms or via RDC to the server - Reference the 'Information to create a ticket' within the 'Hughes NOC Spreadsheet.' for the correct device, gateway, and services needed to be escalated. - Timing issues are typically to be escalated to the Network_Infrastructure team. - The NMC Daily Logs have the correct NOC Spreadsheet for the correct team to escalate to.",
        'VSAT Outages/Down': "Check the performance metrics for any ongoing issues.",
        'Decommission Requests': "Gather the SID and Serial numbers of the terminal that is to be decommissioned., - Log into the corresponding Vision server via NOC_FORMS (Quickest) or via RDC to the Server itself., - Navigate to the ACS Lite tab, select Manual Decommission then input the SID, Serial, Your operator name, Requester name (FSS, WWTS, etc) is fine, - Requester Department is the same as Requester name, and the Reason code for ALL Decommissions is C22 - Decommissioned: Technical Troubleshooting. - Then Execute the process, allow for the server to respond, then copy the 'Successful Decommision' information into the service ticket for closure.",
        'Compose New': 'Restart the device and check if it resolves the issue.',
        'IGT DHCP Pool Purge': "IGT NOC Vision DHCP Pool Purge. - Log into the NOC_'x' Vision box. - Search in the startmenu for 'Telnet <ip>'. Replace <ip> with the IP address to connect to. - Using the following: brighton:swordfish to gain access. - Within the CLI type: cd '/cfg0/' - ls -lta - rm 'dhcpsact.txt' - ls -lta -> Should no longer display the dhcp file.",
        'IGT site not downloading': "Log into the UEMVision box and open the 'Task Manager', and navigate to the 'Services' tab. - Look for these 3 services that need to be restarted, - JservicesFGN - JservicesGENSDL - JservicesGENSDL MGR, - If the NOC_View and Satellite Router View are not loading - Restart the service -- JservicesTOPO",
        'XCI Issues': "Typically, issues with XCI are 'seen' via the SL1 board OR via emails from Dhruval. - Create a ticket with the information provided by Dhurval or SL1. - Escalate the issue to XCI_Support engineers, and follow up until case is resolved. ",
        'SDG': 'Call 1-(866)-245-7059',
        'CNE-GW': 'Call (301)-601-4140',
        'CNE-NMS': 'Call (240)-760-2132',
        'NI': 'Call (301)-601-2624 | Secondary (301)-428-5809',
        'ESE [ENOC]': 'Call Ext "884143 OR 884144',
        'EDSE': 'Call Ext "884110 OR 884111',
        'HNSec': 'Call (301)-601-4128',
        'HNSoc': 'Call (301)-601-2666.',
        'Jupiter 1 & 2': 'Jupiter 1&2 JOVIAN -> username:PIN+RSA | NAD DSS -> hns-username:PIN+RSA',
        'Jupiter 3': 'Jupiter 3 DSS & JOVIAN -> Use your provisioned username and password',
        'Ku & Terrestrial': 'For KU use the NOC_FORMS for Decommissions, and RDC into the specific servers for other issues. (ie: Timing and Power, etc.)',
        'SA_Template': 'Contact the admin for site access approval.'
    }

    if main_choice == 'Email Template':
        values = [entry.get() for entry in input_fields[main_choice]]
        if len(values) == 4:
            generate_email_template(*values)
    elif main_choice == 'Event Summary':
        values = [entry.get() for entry in input_fields[main_choice]]
        if len(values) == 11:
            generate_event_template(*values)
    elif main_choice == 'Site Access Requests':
        showinfo('Site Access Request', 'Site Access Request template has been processed.')
    else:
        message = procedures_dict.get(selected_option, "No information available.")
        showinfo('Procedure Info', message)

    submenu_window.destroy()

def show_main_menu():
    Label(window, text="Welcome to the NMC Assistance Framework Application", font=('Helvetica 16 bold')).pack(pady=10)
    Label(window, text="Created by Jamie Valentonis", font=('Helvetica 16 bold')).pack(pady=10)
    
    choices = ['Phone Calls', 'J1/2 Issues', 'J3/FUSION', 'Ku Issues', 'Email Template', 'IGT/XCI Issues', 'Escalation Pathes', 'Tool Login info', 'Event Summary', 'Site Access Requests']
    
    combo = Combobox(window, values=choices)
    combo.set(choices[0])
    combo.bind("<<ComboboxSelected>>", lambda event: show_submenu(combo.get()))
    combo.pack(pady=20)

show_main_menu()
window.mainloop()
