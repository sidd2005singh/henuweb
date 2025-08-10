import streamlit as st
import boto3
import json

st.title("☁ AWS Automation Panel")

# Load credentials from config
with open("config.json") as f:
    config = json.load(f)

aws_access_key = config["AWS"]["ACCESS_KEY"]
aws_secret_key = config["AWS"]["SECRET_KEY"]
region = config["AWS"]["REGION"]

ec2 = boto3.client(
    'ec2',
    region_name=region,
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

task = st.selectbox("Select AWS Task", ["Launch EC2", "Terminate EC2", "View CloudWatch Logs"])

if task == "Launch EC2":
    ami_id = st.text_input("AMI ID", "ami-090fa75af13c156b4")
    instance_type = st.text_input("Instance Type", "t2.micro")
    key_name = st.text_input("Key Pair Name")
    if st.button("Launch Instance"):
        res = ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            KeyName=key_name,
            MinCount=1,
            MaxCount=1
        )
        st.success(f"Launched Instance ID: {res['Instances'][0]['InstanceId']}")

elif task == "Terminate EC2":
    instance_id = st.text_input("Instance ID")
    if st.button("Terminate Instance"):
        ec2.terminate_instances(InstanceIds=[instance_id])
        st.warning(f"Terminated Instance: {instance_id}")

elif task == "View CloudWatch Logs":
    logs = boto3.client(
        'logs',
        region_name=region,
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    group = st.text_input("Log Group Name")
    stream = st.text_input("Log Stream Name")
    if st.button("Fetch Logs"):
        events = logs.get_log_events(
            logGroupName=group,
            logStreamName=stream,
            startFromHead=True
        )
        for e in events['events']:
            st.text(e['message'])
