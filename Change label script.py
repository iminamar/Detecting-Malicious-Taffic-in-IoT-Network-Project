# import pandas as pd


# # this code is for class 2
# def modify_label_column(input_file, output_file, label_mapping):
#     # Read the CSV file into a pandas DataFrame
#     df = pd.read_csv(input_file)
    
#     # Modify the values in the 'label' column based on the provided mapping
#     df['label'] = df['label'].map(label_mapping).fillna(df['label'])
    
#     # Write the modified DataFrame back to a new CSV file
#     df.to_csv(output_file, index=False)

# # Define the provided dictionary mapping old label values to new label values
# dict_2classes = {
#     'DDoS-RSTFINFlood': 'Attack',
#     'DDoS-PSHACK_Flood': 'Attack',
#     'DDoS-SYN_Flood': 'Attack',
#     'DDoS-UDP_Flood': 'Attack',
#     'DDoS-TCP_Flood': 'Attack',
#     'DDoS-ICMP_Flood': 'Attack',
#     'DDoS-SynonymousIP_Flood': 'Attack',
#     'DDoS-ACK_Fragmentation': 'Attack',
#     'DDoS-UDP_Fragmentation': 'Attack',
#     'DDoS-ICMP_Fragmentation': 'Attack',
#     'DDoS-SlowLoris': 'Attack',
#     'DDoS-HTTP_Flood': 'Attack',
#     'DoS-UDP_Flood': 'Attack',
#     'DoS-SYN_Flood': 'Attack',
#     'DoS-TCP_Flood': 'Attack',
#     'DoS-HTTP_Flood': 'Attack',
#     'Mirai-greeth_flood': 'Attack',
#     'Mirai-greip_flood': 'Attack',
#     'Mirai-udpplain': 'Attack',
#     'Recon-PingSweep': 'Attack',
#     'Recon-OSScan': 'Attack',
#     'Recon-PortScan': 'Attack',
#     'VulnerabilityScan': 'Attack',
#     'Recon-HostDiscovery': 'Attack',
#     'DNS_Spoofing': 'Attack',
#     'MITM-ArpSpoofing': 'Attack',
#     'BenignTraffic': 'Benign',
#     'BrowserHijacking': 'Attack',
#     'Backdoor_Malware': 'Attack',
#     'XSS': 'Attack',
#     'Uploading_Attack': 'Attack',
#     'SqlInjection': 'Attack',
#     'CommandInjection': 'Attack',
#     'DictionaryBruteForce': 'Attack'
# }

# # Example usage:
# input_file = "8 classes.csv"
# output_file = "8 classes new.csv"
# modify_label_column(input_file, output_file, dict_2classes)







# ------------------------------------------------------------------------------------------


import pandas as pd

def modify_label_column(input_file, output_file, label_mapping):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Modify the values in the 'label' column based on the provided mapping
    df['label'] = df['label'].map(label_mapping).fillna(df['label'])
    
    # Write the modified DataFrame back to a new CSV file
    df.to_csv(output_file, index=False)

# Define the provided dictionary mapping old label values to new label values
dict_7classes = {
    'DDoS-RSTFINFlood': 'DDoS',
    'DDoS-PSHACK_Flood': 'DDoS',
    'DDoS-SYN_Flood': 'DDoS',
    'DDoS-UDP_Flood': 'DDoS',
    'DDoS-TCP_Flood': 'DDoS',
    'DDoS-ICMP_Flood': 'DDoS',
    'DDoS-SynonymousIP_Flood': 'DDoS',
    'DDoS-ACK_Fragmentation': 'DDoS',
    'DDoS-UDP_Fragmentation': 'DDoS',
    'DDoS-ICMP_Fragmentation': 'DDoS',
    'DDoS-SlowLoris': 'DDoS',
    'DDoS-HTTP_Flood': 'DDoS',
    'DoS-UDP_Flood': 'DoS',
    'DoS-SYN_Flood': 'DoS',
    'DoS-TCP_Flood': 'DoS',
    'DoS-HTTP_Flood': 'DoS',
    'Mirai-greeth_flood': 'Mirai',
    'Mirai-greip_flood': 'Mirai',
    'Mirai-udpplain': 'Mirai',
    'Recon-PingSweep': 'Recon',
    'Recon-OSScan': 'Recon',
    'Recon-PortScan': 'Recon',
    'VulnerabilityScan': 'Recon',
    'Recon-HostDiscovery': 'Recon',
    'DNS_Spoofing': 'Spoofing',
    'MITM-ArpSpoofing': 'Spoofing',
    'BenignTraffic': 'Benign',
    'BrowserHijacking': 'Web',
    'Backdoor_Malware': 'Web',
    'XSS': 'Web',
    'Uploading_Attack': 'Web',
    'SqlInjection': 'Web',
    'CommandInjection': 'Web',
    'DictionaryBruteForce': 'BruteForce'
}

# Example usage:
input_file = "8 classes.csv"
output_file = "8 classes new.csv"
modify_label_column(input_file, output_file, dict_7classes)

print("\n..........complete........\n")
