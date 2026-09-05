# What Is a Transaction?

A transaction is a group of one or more database operations that are treated as one logical unit of work. <br>
For example, imagine transferring ₹1,000 from: <br>

Account A → Account B <br>

You need two operations: <br>

```text
UPDATE accounts
SET balance = balance - 1000
WHERE id = 1;
```

 <br>

 ```text
UPDATE accounts
SET balance = balance + 1000
WHERE id = 2;
```

 <br>
These two operations are logically one operation: <br>

Transfer ₹1,000 <br>
 <br> 
You don't want this situation: <br>

```text
A loses ₹1,000
        ↓
B does NOT receive ₹1,000
```

 <br>
That would be a serious data inconsistency.
 <br>
Instead: <br>

```text
START TRANSACTION
       ↓
Debit A
       ↓
Credit B
       ↓
Everything successful?
    ↙           ↘
  YES            NO
   ↓              ↓
 COMMIT         ROLLBACK
```

 <br>
That's the purpose of a transaction.

---

# Real-Life Example

Think about booking a flight. <br>

Suppose the system needs to: <br>

Reserve a seat <br>
Create the booking <br>
Record the payment <br>
Update the available-seat count <br>

These operations are related. <br>

Imagine: <br>

Seat reserved       ✅ <br>
Booking created     ✅ <br>
Payment recorded    ❌ <br>

If the system simply continues, you could end up with a reserved seat but no successful payment. <br>
 <br>
A transaction allows the system to say: <br>

Either the complete operation succeeds, or the database returns to the previous consistent state. <br>

---

# Basic Transaction Commands

The three commands you should know first are: <br>

```text
BEGIN;
```

<br>

```text
COMMIT;
```

<br>

```text
ROLLBACK;
```

---

# BEGIN

BEGIN starts a transaction. <br>

```text
BEGIN;
```

 <br>

Then you perform your operations: <br>

```text
UPDATE accounts
SET balance = balance - 1000
WHERE id = 1;
```

 <br>

 ```text
UPDATE accounts
SET balance = balance + 1000
WHERE id = 2;
```

---

# COMMIT

If everything is successful: <br>

```text
COMMIT;
```

 <br>

COMMIT makes the transaction's changes permanent. <br>

Conceptually: <br>

```text
BEGIN
 ↓
Operations
 ↓
COMMIT
 ↓
Changes saved
```

---

# ROLLBACK

If something goes wrong: <br>

```text
ROLLBACK;
```

The changes made during the transaction are undone. <br>

Conceptually: <br>

```text
BEGIN
 ↓
Operation 1 ✅
 ↓
Operation 2 ❌
 ↓
ROLLBACK
 ↓
Undo transaction changes
```

---

# Complete Example

Suppose we have: <br>

```text
accounts
----------------------
id | name | balance
----------------------
1  | A    | 5000
2  | B    | 3000
```

We want to transfer ₹1,000 from A to B.<br>

```text
BEGIN;
```

<br>

```text
UPDATE accounts
SET balance = balance - 1000
WHERE id = 1;
```

<br>

```text
UPDATE accounts
SET balance = balance + 1000
WHERE id = 2;
```

<br>

```text
COMMIT;
```

<br>
Result: <br>

A = 4000 <br>
B = 4000 <br>

The transaction succeeded. <br>

## What If Something Goes Wrong?

Suppose the first operation succeeds: <br>

```text
UPDATE accounts
SET balance = balance - 1000
WHERE id = 1;
```

 <br>
 
but something goes wrong before the second operation. <br>

We can do: <br>

```text
ROLLBACK;
```

 <br>
 
The database returns the transaction's changes to the state before the transaction began. <br>

So: <br>

```text
Before:
A = 5000
B = 3000
```

 <br>

 ```text
After rollback:
A = 5000
B = 3000
```


## Why Transactions Are Needed

Without transactions: <br>

```text
Operation 1 → SUCCESS
Operation 2 → FAILURE
```

 <br>
 
You may end up with partially completed work. <br>

With transactions: <br>

```text
Operation 1 → SUCCESS
Operation 2 → FAILURE
       ↓
ROLLBACK
       ↓
No partial transaction result
```

 <br>
This is why transactions are essential for operations that must remain consistent.

---

# ACID

A reliable database transaction follows the ACID properties: <br>

```text
A → Atomicity
C → Consistency
I → Isolation
D → Durability
```

---


