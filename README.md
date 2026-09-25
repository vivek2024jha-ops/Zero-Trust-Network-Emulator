# Zero-Trust-Network-Emulator


# Zero-Trust-Network-Emulator

## Project Overview

The Zero-Trust Network Emulator is a Python-based cybersecurity project
designed to demonstrate the basic principles of a Zero Trust security model.

The project simulates user authentication, role-based authorization,
least-privilege access control, credential rotation, and security alerting
within a controlled environment.

Instead of automatically trusting users after authentication, each access
request is verified before allowing access to a protected resource.

This project provides a practical foundation for understanding Zero Trust
security concepts and basic access-control mechanisms used in cybersecurity
environments.

# Objectives

- Understand the basic principles of Zero Trust security
- Implement user authentication
- Implement role-based access control
- Apply least-privilege access policies
- Detect unauthorized access attempts
- Implement credential rotation
- Generate security alerts for suspicious activity
- Maintain basic audit-style access logs
- Understand how Zero Trust controls can be applied to network resources

## Lab Environment

| Component | Details |
|-----------|---------|
| Operating System | Windows |
| Programming Language | Python 3 |
| Development Environment | Visual Studio Code |
| Project Type | Security Emulator |
| Access Model | Zero Trust / Least Privilege |

## Tools Used

- Python 3 – Used to develop the security emulator
- Python `secrets` module – Used for secure credential generation
- Authentication Logic – Used to verify user credentials
- Role-Based Access Control – Used to control resource permissions
- Credential Rotation – Used to generate new credentials
- Console Logging – Used to monitor access activity
- Visual Studio Code – Used for development and testing

## Security Scenario

A controlled network environment was simulated with different users,
roles, and protected resources.

The emulator verifies every access request before granting access.
An authenticated user can only access resources permitted for their role.

For example, an analyst user is allowed to access log resources but is
not allowed to access the database.

The system also detects failed authentication and unauthorized access
attempts and generates security alert messages.

## Implementation Process

### Step 1 - User Authentication

The emulator verifies the username and credential provided with each
access request.

Invalid authentication attempts are rejected and recorded as security
events.

### Step 2 - Role-Based Authorization

After successful authentication, the user's role is checked against the
defined access policy.

Different roles have access to different resources based on the
least-privilege principle.

### Step 3 - Access Control

The emulator allows access only when the requested resource is included
in the user's authorized resource list.

Unauthorized requests are denied.

### Step 4 - Security Alerts

When authentication fails or a user attempts to access an unauthorized
resource, the emulator generates a security alert message.

These alerts simulate how suspicious access activity could be forwarded
to a security monitoring or alerting platform.

### Step 5 - Credential Rotation

The emulator generates a new credential using Python's secure random
credential-generation functionality.

The credential is rotated during the simulation to demonstrate how
credential rotation can reduce the risk associated with long-lived
credentials.

### Step 6 - Access Logging

The emulator records access activity with timestamps and information
about the user, role, requested resource, and access result.

This provides basic audit information for security monitoring.

## Zero-Trust Architecture

```mermaid
flowchart LR
    U[User / Device] --> Z[Zero-Trust Access Layer]

    Z --> A[Authentication]
    A --> P[Authorization / Least Privilege]

    P -->|Allowed| R[Protected Resources]
    P -->|Denied| D[Access Denied]

    Z --> C[Credential Rotation]
    C --> CS[Credential Store]

    D --> AL[Security Alert]
    AL --> S[Slack Alert Simulation]

    Z --> L[Audit Logs]






















## Architecture

```mermaid
flowchart LR
    U[User / Device] --> Z[Zero-Trust Access Layer]

    Z --> A[Authentication]
    A --> P[Authorization / Least Privilege]

    P -->|Allowed| R[Protected Resources]
    P -->|Denied| D[Access Denied]

    Z --> C[Credential Rotation]
    C --> CS[Credential Store]

    D --> AL[Security Alert]
    AL --> S[Slack Alert]



Security Principles
Verify every access request
Least-privilege authorization
Authentication before resource access
Credential rotation
Security alerts for suspicious activity
Audit logging
Disclaimer

This project is an educational security emulator and does not
represent a production network security system.
    Z --> L[Audit Logs]
