<div align="center"> 
<img width="50%" height="50%" src="https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/images/selenium-python-logo.png" hspace="10">
</div>

# Selenium (Python) Automation for <a href="https://edalnice.cz/en/bulk-purchase/index.html#/multi_eshop/batch">Bulk purchase of Vignette</a>

<div align="center"> 
<img width="90%" height="90%" src="https://github.com/harshjainsk/Python-Automation-Using-Selenium/blob/main/images/vigenette-automation.gif" hspace="10">
</div>

An example of placing an order without human intervention by running a <a href="https://github.com/harshjainsk/Python-Automation-Using-Selenium/blob/main/main.py">python script</a>

**Main Objectives**<br/>
- The main purpose is to demonstrate the professional abilities of writing browser automation using the Python language with Selenium.<br/>
- Build fast and readable automation using minimal code<br/>
- Showcase with effective way to identify web elements<br/>

### <a id="about"></a>About the project:<br/>
This project was built to automate the process of ordering vignettes in bulk. The <a href="https://github.com/harshjainsk/Python-Automation-Using-Selenium/blob/main/main.py">python script</a> automatically fills
various data fields in the <a href="https://edalnice.cz/en/bulk-purchase/index.html#/multi_eshop/batch">website</a> such as:

- Name of the country
- Vignette validity
- License plate number
- Type of Vignette
- If the vehicle is powered by natural gas or biomethane(optional field)


<div align="center"> 
<img width="90%" height="90%" src="https://github.com/harshjainsk/Python-Automation-Using-Selenium/blob/main/images/order-placement.gif" hspace="10">
</div>

<br>
Once, all data is uploaded using the script, it will click on continue and fill the contact details of the erson associated with order. The details to be filled in this page are as follows:

- email id
- confirmation of email id
- Mode of payment
- It will also click on checkbox for accepting the terms and conditions

<div align="center"> 
<img width="90%" height="90%" src="https://github.com/harshjainsk/Python-Automation-Using-Selenium/blob/main/images/adding-email-payment-method.gif" hspace="10">
</div>

<br>
As the script clicks on pay, we need to upload the following:

- Card number
- Validity of card
- CVV

The above details are read from [config.py](https://github.com/harshjainsk/Python-Automation-Using-Selenium/blob/main/config.py)
<div align="center"> 
<img width="90%" height="90%" src="https://github.com/harshjainsk/Python-Automation-Using-Selenium/blob/main/images/card-details.gif" hspace="10">
</div>

## NOTE:
```
If you ever try to run this script, please change the dates in sample.csv in order to run the script successfully.
```
