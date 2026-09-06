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

# A — Atomicity

Atomicity means: <br>

A transaction is treated as one indivisible unit: either all required changes happen, or none of them do. <br>

Think: <br>

```text
ALL
or
NOTHING
```

Example: <br>

```text
Transfer ₹1,000

Debit A       ✅
Credit B      ❌
```

Atomicity ensures the transaction doesn't leave behind only the debit as the final committed result. <br>

Conceptually: <br>

```text
Transaction
   |
   ├── Operation 1
   ├── Operation 2
   └── Operation 3
          ↓
     All succeed
          ↓
       COMMIT

OR

     Any failure
          ↓
       ROLLBACK
```

Easy way to remember <br>

Atomicity = All or Nothing <br>

---

# C — Consistency

Consistency means: <br>

A transaction should take the database from one valid state to another valid state while preserving defined rules and constraints. <br>

Suppose: <br>
 <br>
balance >= 0
 <br>
is a business rule.

Before transaction:
 <br>
A = ₹5,000 <br>
B = ₹3,000 <br>

After transferring ₹1,000: <br>

A = ₹4,000 <br>
B = ₹4,000 <br>

The database remains valid. <br>
 <br>
Consistency can involve:
 <br>

 ```texxt
Primary key constraints
Foreign key constraints
Unique constraints
CHECK constraints
Data types
Business rules enforced by the application/database
```

Easy way to remember
 <br>
Consistency = Database remains valid
 <br>

 ---

# I — Isolation

This is usually the hardest ACID property for beginners. <br>

Isolation means: <br>

Concurrent transactions should not improperly interfere with each other's intermediate states. <br>

Imagine two users accessing the database at the same time. <br>

```text
Transaction A
       ↘
       Database
       ↗
Transaction B
```

Both transactions may be executing concurrently. <br>

The database needs rules controlling what one transaction can see from another. <br>

## Why Isolation Is Needed

Suppose account A has: <br>

₹5,000 <br>

Transaction 1 is updating it. <br>

At roughly the same time, Transaction 2 reads the account. <br>

If Transaction 2 can see uncommitted intermediate changes, it could make decisions based on data that later gets rolled back. <br>

That's a problem. <br>

Isolation helps control these concurrency issues. <br>

---
# D — Durability

Durability means: <br>

Once a transaction has successfully committed, its committed changes should survive subsequent failures, such as a database/server crash, subject to the database system's durability guarantees. <br>

Example: <br>

```text
Payment transaction
       ↓
COMMIT
       ↓
Database/server crashes
       ↓
Database recovers
       ↓
Committed transaction remains
```

This is achieved through mechanisms such as: <br>

```text
Write-ahead logging
Recovery mechanisms
Persistent storage
Replication and backup strategies in larger architectures
```

Easy way to remember <br>

Durability = Committed means it survives recovery <br>

---

# Atomicity vs Consistency

These two are commonly confused. <br>

**Atomicity** <br>

Deals with the transaction as a unit:<br>

```text
Did all required operations happen,
or did the transaction get rolled back?
```

<br>

**Consistency** <br>

Deals with database correctness:<br>

```text
Did the database remain within its
defined valid rules?
```

<br>
Example:<br>

Transfer money<br>
<br>
Atomicity:<br>

Don't permanently debit one account without the corresponding credit.<br>
<br>
Consistency:<br>

The database's integrity constraints and business invariants remain valid.<br>


<br><br>

# Atomicity vs Durability

**Atomicity** <br>

```text
Transaction fails
↓
Changes aren't committed as the transaction's final result
```
 
 <br>
 
**Durability**  <br>

```text
Transaction succeeds
↓
COMMIT
↓
Changes survive recovery
```

 <br>
So: <br>

Atomicity → What happens when transaction succeeds/fails as a unit? <br>

Durability → What happens after successful COMMIT? <br>

---

# Isolation Levels

Databases provide different isolation levels. <br>

In PostgreSQL, the standard transaction isolation levels exposed to users are: <br>

```text
READ COMMITTED
REPEATABLE READ
SERIALIZABLE
```

 <br>
PostgreSQL also accepts READ UNCOMMITTED, but it behaves like READ COMMITTED. <br>

The higher the isolation, generally the stronger the protection against certain concurrency anomalies, but stronger guarantees can come with more contention or retries. <br>

---

# Read Phenomena

Before understanding isolation levels, understand these terms. <br>

**Dirty Read**  <br>

Transaction A changes data but hasn't committed. <br>

Transaction B reads that uncommitted data. <br>

Then Transaction A rolls back. <br>

Now B read something that never became committed. <br>

Conceptually: <br>

```text
Transaction A
UPDATE
  ↓
Uncommitted

Transaction B
  ↓
Reads A's uncommitted value ❌
```

 <br>
PostgreSQL's normal isolation behavior does not allow dirty reads. <br> <br>

# Non-Repeatable Read

Suppose Transaction A reads: <br>

balance = 5000 <br>

Then Transaction B updates it: <br>

balance = 4000 <br>
COMMIT <br>

Transaction A reads again: <br>

balance = 4000 <br>

The same transaction got different results from the same row. <br>

That's a non-repeatable read. <br> <br>

# Phantom Read

Suppose Transaction A runs: <br>

```text
SELECT *
FROM users
WHERE age >= 18;
```

 <br>
It gets: <br>

100 rows <br>

Transaction B inserts another matching user and commits. <br>

Transaction A runs the query again and gets: <br>

101 rows
 <br>
The new matching row is a phantom from Transaction A's perspective. <br>

---

# PostgreSQL's Default Isolation Level

PostgreSQL's default transaction isolation level is: <br>

READ COMMITTED

Under READ COMMITTED, each statement generally sees a snapshot of data committed before that statement began.

This means a later statement within the same transaction can see newly committed changes from other transactions.

Example:

BEGIN

Statement 1 → sees committed state A

Other transaction commits change

Statement 2 → can see the newly committed state

This is why READ COMMITTED does not guarantee repeatable reads across the entire transaction.



















 
