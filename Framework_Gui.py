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
    subject_text.config(state=NORMAL)

    Label(email_template_window, text="Email Body:", font=('Helvetica 12 bold')).pack(anchor=W, padx=10, pady=5)
    body_text = Text(email_template_window, wrap=WORD)
    body_text.pack(padx=10, pady=5, fill=BOTH, expand=True)
    body_text.insert(END, email_body)
    body_text.config(state=NORMAL)

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
        event_text.config(state=NORMAL)

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
        'Single sites': "The site SAN, and the SERIAL numbers of the terminal(s) -> There may be more than one - Log into DSS (hns-username:PIN+RSA) and navigate the sidebar to 'Jupiter Dashboard' - Select 'Jupiter Dashboard', then enter the SAN or the ESN of the site into DSS to gather more information, - such as the IP address, and site details.",
        'Terminal drops': "The site's SAN, and ESN(s), Enter the site's SAN or ESN into DSS and navigate to the 'Jupiter Dashboard' and select 'All Terminals'.",
        'BGP Peering': 'Contact NCCM, [Phone Number], or use the NMS dashboard to view BGP peering information.',
        'Move Allows': 'Use the DSS tool to access the site\'s SAN and ESN(s), navigate to the Jupiter Dashboard, and access the Move Allows section.',
        'J3_Single sites': 'Gather site SAN, SERIAL numbers, log into DSS, navigate to "J3 Dashboard", and select "Single Site" for detailed information.',
        'J3_Terminal drops': 'Gather SAN and ESN(s), log into DSS, and navigate to "J3 Dashboard" for terminal status.',
        'J3_BGP Peering': 'Use the NMS dashboard for J3 BGP peering info or contact NCCM.',
        'J3_Move Allows': 'Gather SAN and ESN(s), log into DSS, navigate to "J3 Dashboard", and access the Move Allows section.',
        'Enterprise': 'Ensure all Ku band devices are connected and operational, refer to the Enterprise manual.',
        'Timing/Power': 'Check and adjust timing and power settings as per the Ku band documentation.',
        'VSAT Outages/Down': 'Log into the VSAT monitoring system, check for alerts, and follow the outage handling procedures.',
        'Decommission Requests': 'Submit decommission requests through the official portal, including all necessary details.',
        'CAC Key Upload': 'Log into the CAC management tool and follow the upload instructions.',
        'IGT DHCP Pool Purge': 'Access the IGT management system, navigate to DHCP settings, and perform the pool purge.',
        'IGT site not downloading': 'Verify network connections, check IGT site configuration, and refer to the troubleshooting guide.',
        'XCI Issues': 'Refer to the XCI manual, verify configurations, and check logs for errors.',
        'SDG': 'Refer to the SDG escalation path document and follow the steps.',
        'CNE-GW': 'Refer to the CNE-GW escalation path document and follow the steps.',
        'CNE-NMS': 'Refer to the CNE-NMS escalation path document and follow the steps.',
        'NI': 'Refer to the NI escalation path document and follow the steps.',
        'ESE [ENOC]': 'Refer to the ESE [ENOC] escalation path document and follow the steps.',
        'EDSE': 'Refer to the EDSE escalation path document and follow the steps.',
        'HNSec': 'Refer to the HNSec escalation path document and follow the steps.',
        'HNSoc': 'Refer to the HNSoc escalation path document and follow the steps.',
        'Jupiter 1 & 2': 'Ensure you have the latest credentials for Jupiter 1 & 2 systems, and log in through the official portal.',
        'Ku & Terrestrial': 'Use the latest credentials for Ku & Terrestrial systems, accessible via the dedicated login page.',
        'Jupiter 3': 'Log into Jupiter 3 using the current credentials and follow the access procedures.'
    }

    if main_choice in ['Email Template', 'Event Summary']:
        input_values = [entry.get() for entry in input_fields[main_choice]]
        if main_choice == 'Email Template':
            if len(input_values) == 4:
                generate_email_template(*input_values)
            else:
                showinfo('Error', 'Please provide all the required input values for the Email Template.')
        elif main_choice == 'Event Summary':
            if len(input_values) == 12:
                generate_event_template(*input_values)
            else:
                showinfo('Error', 'Please provide all the required input values for the Event Summary.')
    else:
        procedure = procedures_dict.get(selected_option, "No procedure available for this option.")
        Label(submenu_window, text=f'Procedure:\n{procedure}', font=('Helvetica 12')).pack(pady=10)
        
    Button(submenu_window, text="Close", command=submenu_window.destroy).pack(pady=10)

label = Label(window, text="Please select an option:", font=('Helvetica 16 bold'))
label.pack(pady=10)

options = ['Phone Calls', 'J1/2 Issues', 'J3/FUSION', 'Ku Issues', 'Email Template', 'IGT/XCI Issues', 'Escalation Pathes', 'Tool Login info', 'Event Summary', 'Site Access Requests']
combo = Combobox(window, values=options)
combo.pack(pady=10)

def on_submit():
    selected_choice = combo.get()
    if selected_choice:
        show_submenu(selected_choice)
    else:
        showinfo('Error', 'Please select an option from the dropdown menu.')

submit_button = Button(window, text="Submit", command=on_submit)
submit_button.pack(pady=10)

clear_button = Button(window, text="Clear", command=clear)
clear_button.pack(pady=10)

window.mainloop()
