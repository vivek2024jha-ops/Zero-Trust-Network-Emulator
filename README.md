# Zero-Trust-Network-Emulator























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

    Z --> L[Audit Logs]
