# AppMix Builder Script

## Overview

The appmix_builder.py script creates an application mix from a CSV file containing application names and their corresponding percentages or weights.

## How it Works
The script reads the application names from the CSV file and searches for corresponding applications in the CyPerf library. If a match is found, the application is added to the CyPerf app mix using the percentage or weight for the corresponding application.

The script provides a percentage coverage based on the matches. For example, if 10 applications were provided in the CSV and 5 were found in the CyPerf library, the percentage coverage would be (5/10) * 100 = 50%.

## Features
+ Creates application mix from CSV file
+ Searches for applications in CyPerf library
+ Provides percentage coverage based on matches
+ Option to use capture-to-application converter to increase coverage percentage
+ Option to configure test or abort
## Capture-to-Application Converter

The user can upload a set of captures (corresponding to applications that were not present in the CyPerf library) to a pre-configured location (folder) and the converter function will create applications and add them to the CyPerf library. This may help to increase the coverage percentage.
## Application Naming Convention
Applications created by the script are named CCA-<pcap-name>. All applications can be found in the Resource Library section of the CyPerf controller.
## Steps to Run the Script
### Step 1: Configure Test Parameters

1. Edit the test_parameters.yml file under the "cyperf-api-wrapper/samples" folder.
Set the variable named "location_of_folder_containing_captures" to the absolute path of the folder where all captures should be stored.

2. Set the variable named "location_of_folder_containing_captures" to the absolute path of the folder where all captures should be stored.

### Step 2: Run the Script

1. Navigate to the folder: cyperf-api-wrapper.

2. Run the script "appmix_builder.py" using the following command from the CLI:
   ```bash
   python3.x samples/appmix_builder.py --controller <IP address of CyPerf controller> -- 
   license-server <IP address of License server> --user <username>  --password <password> 
Example:
   ```bash
   python3.13 samples/appmix_builder.py --controller 10.39.68.180 --license-server 10.39.68.180 --license-user admin  --license-password CyPerf\&Keysight#1

