FINTRACK PRO – CLI Finance Manager

FinTrack Pro is a Command Line Interface (CLI) based Personal Finance Management System built using **Python, SQLite, and SQLAlchemy ORM**.
This project allows users to manage daily expenses, track subscriptions, set monthly budgets, and generate analytical reports using both ORM and Raw SQL queries.

 Project Overview
FinTrack Pro demonstrates practical implementation of:
- Object Relational Mapping (ORM)
- Database relationships (One-to-Many)
- Raw SQL queries inside ORM projects
- CRUD operations
- CLI-based modular architecture


 Objectives

- Understand ORM-based database interaction  
- Use SQLite with Python  
- Implement CRUD operations  
- Write raw SQL for analytics  
- Design modular CLI architecture  
- Build a real-world finance tracking system  


Technologies Used

- Python  
- SQLite Database  
- SQLAlchemy ORM  
- Raw SQL Queries  
- CLI (Command Line Interface)  

---

 Features

- Add Category  
- Add Expense  
- Update Expense  
- Delete Expense  
- Search Expense by Date  
- Category-wise Expense Report (using Raw SQL)  
- Add Subscription  
- View Subscriptions  
- Set Monthly Budget  
- Budget Alert System  
- Persistent Database Storage  


Database Design
 Tables:

1. **categories**
   - id (Primary Key)
   - name

2. **expenses**
   - id (Primary Key)
   - title
   - amount
   - date
   - category_id (Foreign Key)

3. **subscriptions**
   - id (Primary Key)
   - name
   - amount
   - next_date

4. **budgets**
   - id (Primary Key)
   - month
   - limit

---

### Relationship:

Category (1)  ➝  (N) Expenses  

- One category can have multiple expenses  
- Implemented using `ForeignKey` and `relationship()`  

Sample Raw SQL Used

```sql
SELECT c.name, SUM(e.amount)
FROM categories c
JOIN expenses e
ON c.id = e.category_id
GROUP BY c.name;
```
This query generates category-wise total expense reports.
---
 CLI Menu

```
----FINTRACK PRO----
1. Add Category
2. Add Expense
3. Update Expense
4. Delete Expense
5. Search Expense by Date
6. Category Expense Report
7. Set Monthly Budget
8. Budget Alert
9. Add Subscription
10. View Subscriptions
11. Exit
```
 Learning Outcomes

- Strong understanding of SQLAlchemy ORM  
- Implementation of One-to-Many relationships  
- Writing Raw SQL inside ORM-based projects  
- Aggregation using GROUP BY  
- Modular CLI application development  
- Real-world database design
- 
Future Enhancements

- CSV Export  
- Web Interface using Flask  
- User Authentication  
- Graphical Analytics Dashboard  
- Email Budget Notifications  

 Author

Anshika Singh  
3rd Year Student  
FINTRACK PRO – 1st Assignment Project
