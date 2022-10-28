- [Installation](#installation)

### Installation

#### Clone repo

``` bash
# clone the repo
$ git clone https://github.com/Huxteen/supply-chain-app.git

# go into app's directory
$ cd supply-chain-app

# Build docker-compose
$ docker-compose build

## Run test and Flake8
$ docker-compose run app sh -c "python manage.py test && flake8"

# start project
$ docker-compose up

# API Documentation Endpoint
 {{base_url}}/swagger/schema/



 


## About Supply Chain App
The supply chain app has a list of product and customer can order our product using their phone. This project is the backend that supply the data to the mobile app. The backend comprises of different app that make up this project namely:
    - [Accounts].
    - [Products].
    - [Address].
    - [Orders].


# Accounts App
The account app is responsible for managing customers within the application to register within the app the users would need to provide their.
    - [Email].
    - [Password].
    - [First_name].
    - [Last_name].

## The Account Endpoints
## create User ['POST]
    {{base_url}}api/accounts/create/

## Login user to get token ['POST']
    {{base_url}}api/accounts/token/

## Retrieve Login user details ['GET]
    {{base_url}}api/accounts/update/

## Update Login user details ['PUT', 'PATCH']
    {{base_url}}api/accounts/update/


# Products App
The product app is responsible for managing products within the application, for customers to make orders based on the preferred product choice. The data for the product schema are:
    - [Name].
    - [User_id].
    - [Price].
    - [Quantity_in_stock].

The product app can perform the CRUD operation. Creating ['POST'] and Updating ['PUT', 'PATCH'] product can only be performed by Admins within the system. All customers can view all the product available within the system.

## The Product Endpoint
## List Product ['GET']
    {{base_url}}api/products/

## Create Product ['POST']
    {{base_url}}api/products/

## Product Detail View ['GET']
    {{base_url}}api/products/{id}/

## Update Product View ['PUT', 'PATCH']
    {{base_url}}api/products/{id}/


# Order App
The order app is responsible for managing customers orders within the application. Customer can select product and the quantity they want to order, they can also select the address they want their item to b delivered to:
    - [order_code].
    - [status].
    - [product_id].
    - [address_id].
    - [unit_price].
    - [quantity].
    - [note].

## Order App Endpoint
## List Order ['GET']
    {{base_url}}api/order/

## Create Order ['POST']
    {{base_url}}api/order/

## Order Detail View ['GET']
    {{base_url}}api/order/{id}/

## Update Order View ['PUT', 'PATCH']
    {{base_url}}api/order/{id}/


# Address App
The adress app is responsible for managing location where customers order would be delivered. Customer can address multiple address.
    - [company_name].
    - [contact_name].
    - [contact_title].
    - [address].
    - [city].
    - [postal_code].
    - [phone].
    - [fax].
    - [user_id].

## Address App Endpoint
## List Address ['GET']
    {{base_url}}api/address/

## Create Address ['POST']
    {{base_url}}api/address/

## Address Detail View ['GET']
    {{base_url}}api/address/{id}/

## Update Address View ['PUT', 'PATCH']
    {{base_url}}api/address/{id}/


# Deployment Instructions for AWS
# Step to Deploy a Docker Container on EC2
    1. SSH onto the EC2 Instance.
    2. Generate a public SSH key for Github SSH permissions.
    3. Copy the EC2 user’s public key.
    4. Add the EC2 public key to the Github account with ownership access to the repository.
    5. Set up the repo on the server.
    6. Start the Docker container.


# Todo
    * Improve test coverage.
    * Add a default address functionality for customers.
    * How to charge the user for their orders.

