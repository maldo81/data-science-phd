# Threat Checklist

- Does untrusted input reach shell, SQL, templates, or dynamic execution?
- Are authorization checks enforced server-side?
- Are sensitive operations protected by explicit confirmation?
- Could this change expose secrets in logs, commits, or telemetry?
- Are failure modes safe and observable?
