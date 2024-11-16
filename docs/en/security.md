# Best Security Practices

## Objectives
Ensure the security of seed phrases by combining secret sharing and encryption.

## General Recommendations

1. **Strong Encryption**:
   - Use robust encryption (AES via `cryptography`).
   - Never share encryption keys.

2. **Secure Storage**:
   - Store files in protected locations, such as physical safes or encrypted storage.
   - Avoid storing sensitive files on unencrypted cloud services.

3. **Multiple Locations**:
   - Store shares in geographically distinct locations.
   - Use multiple secure devices (encrypted USB keys, secure hard drives).

4. **Authentication**:
   - Add authentication steps (password or biometrics) to access files or run the program.

## Technical Best Practices

1. **Offline Execution**:
   - Run the program on an isolated computer, disconnected from the Internet.
   - This minimizes the risk of compromise by malware.

2. **Secure Hardware**:
   - Use trusted devices without suspicious third-party software installed.
   - Prefer secure operating systems (e.g., Tails Linux for security).

3. **Regular Updates**:
   - Keep the libraries used (`shamir-mnemonic`, `cryptography`) up to date to avoid known vulnerabilities.

4. **Delete Temporary Data**:
   - Regularly clean up temporary or unused files using secure deletion tools.

5. **Test Recovery**:
   - Before using the system with real secrets, simulate recovery with test data to ensure the process is robust.

6. **Secret Isolation**:
   - Do not mix sensitive data with other files or folders.
   - Create a dedicated environment for storing and managing shares.

## Project-Specific Recommendations

- **Even-Length Secrets**:
  - Ensure seed phrases in bytes have an even length before splitting them.
- **Secure Deletion**:
  - Use tools like `shred` or `srm` to permanently delete sensitive files after use.

## Reminder
Security is a continuous process. Regularly reassess your practices to ensure your data remains protected.