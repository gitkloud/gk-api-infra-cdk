#!/usr/bin/env python3
import os

import aws_cdk as cdk
from gk_api_infra_cdk.gk_api_infra_cdk import GkCdkStack

app = cdk.App()
GkCdkStack(app, "GkCdkStack")

app.synth()
