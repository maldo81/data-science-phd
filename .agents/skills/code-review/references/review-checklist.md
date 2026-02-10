# Review Checklist

1. Correctness
- Does behavior match intended requirements?
- Are edge cases and failure paths handled?

2. Security
- Are trust boundaries and authorization checks preserved?
- Are untrusted inputs sanitized or constrained?

3. Data and migrations
- Is migration strategy reversible or clearly guarded?
- Could this change corrupt or orphan data?

4. Contracts
- Did request/response or schema changes break callers?
- Are compatibility constraints documented?

5. Tests
- Are important paths tested?
- Are tests meaningful (not just line coverage)?
