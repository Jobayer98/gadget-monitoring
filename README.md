# Django REST API Documentation

## Overview

This Django application provides a RESTful API for managing companies, employees, devices, and device logs. The API is designed to be used by managers, who have specific permissions to perform various actions.

## Authentication

Authentication is required for all API endpoints. The application uses token-based authentication, and users need to include their authentication token in the request header.

## Endpoints

### Companies

#### List and Create Companies

- **Endpoint:** `/api/companies/`
- **Methods:** GET, POST
- **Description:** 
  - GET: Retrieves a list of companies.
  - POST: Creates a new company (available only for users with Manager role).

#### Retrieve, Update, and Delete Company

- **Endpoint:** `/api/companies/<company_id>/`
- **Methods:** GET, PUT, PATCH, DELETE
- **Description:**
  - GET: Retrieves details of a specific company.
  - PUT: Updates the details of a specific company (available only for users with Manager role).
  - PATCH: Partially updates the details of a specific company (available only for users with Manager role).
  - DELETE: Deletes a specific company (available only for users with Manager role).

### Employees

#### List and Create Employees

- **Endpoint:** `/api/employees/`
- **Methods:** GET, POST
- **Description:**
  - GET: Retrieves a list of employees within the user's company.
  - POST: Creates a new employee (available only for users with Manager role).

#### Retrieve, Update, and Delete Employee

- **Endpoint:** `/api/employees/<employee_id>/`
- **Methods:** GET, PUT, PATCH, DELETE
- **Description:**
  - GET: Retrieves details of a specific employee within the user's company.
  - PUT: Updates the details of a specific employee (available only for users with Manager role).
  - PATCH: Partially updates the details of a specific employee (available only for users with Manager role).
  - DELETE: Deletes a specific employee (available only for users with Manager role).

### Devices

#### List and Create Devices

- **Endpoint:** `/api/devices/`
- **Methods:** GET, POST
- **Description:**
  - GET: Retrieves a list of devices within the user's company.
  - POST: Creates a new device (available only for users with Manager role).

#### Retrieve, Update, and Delete Device

- **Endpoint:** `/api/devices/<device_id>/`
- **Methods:** GET, PUT, PATCH, DELETE
- **Description:**
  - GET: Retrieves details of a specific device within the user's company.
  - PUT: Updates the details of a specific device (available only for users with Manager role).
  - PATCH: Partially updates the details of a specific device (available only for users with Manager role).
  - DELETE: Deletes a specific device (available only for users with Manager role).

### Device Logs

#### List and Create Device Logs

- **Endpoint:** `/api/device-logs/`
- **Methods:** GET, POST
- **Description:**
  - GET: Retrieves a list of device logs (available only for users with Manager role).
  - POST: Creates a new device log (available only for users with Manager role).

#### Retrieve, Update, and Delete Device Log

- **Endpoint:** `/api/device-logs/<log_id>/`
- **Methods:** GET, PUT, DELETE
- **Description:**
  - GET: Retrieves details of a specific device log (available only for users with Manager role).
  - PUT: Updates the details of a specific device log (available only for users with Manager role).
  - DELETE: Deletes a specific device log (available only for users with Manager role).

## Permissions

- **IsAuthenticated:** Users must be authenticated to access the API.
- **IsManager:** Users must be authenticated and have the Manager role to perform manager-specific actions.

## Usage Notes

- Include the authentication token in the header of each request.
- Manager permissions are required for certain actions.
- Check the response messages for authorization status.

Feel free to reach out if you have any questions or need further assistance.
