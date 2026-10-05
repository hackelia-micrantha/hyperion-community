# Security policy

Use GitHub private security reporting for suspected credential, private-topology, or deployment-data exposure.

This repository accepts deployment-neutral implementation and synthetic examples only. Real environment configuration, inventories, credentials, encrypted production secrets, key recipients, internal domains, private repository relationships, SSH/Tailscale details, and live service topology belong outside this repository.

CI must not upload Terraform plans or rendered secrets as artifacts. Security fixes target the current `main` branch; no production-support SLA is implied.
