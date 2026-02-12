#1st assignment (FINTRACK PRO-CLI FINANCE MANAGER)

#orm python to sql visa
#session bridge bwt python and db
#relationship connect tables
#raw sql used for reports
#cli menu
#text=write raw sql relationship to links tables,
#decalrative usr to create a base class for tables

#--------------ALL IMPORTS
#use to create database-python connection and write sql queries
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, text

#used to define ORM tables and database session
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

#used to use date
from datetime import date, datetime



#---------DATABASE CONNECTION
#create sqlite database file name fintrack.db
engine=create_engine("sqlite:///fintrack.db")


#base class for orm models
Base=declarative_base()

#session class (acts like cursor)
Session=sessionmaker(bind=engine)

#create session object
session =Session()



#------------table definations

#category table
class Category(Base):
    __tablename__="categories"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    #one category to many expenses/birdirectional
    expenses=relationship("Expense",back_populates="category")

#expense table
class Expense(Base):
    __tablename__="expenses"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    amount=Column(Integer)
    date=Column(Date)
#used foreign key for refrence category id
    category_id=Column(Integer,ForeignKey("categories.id"))
    
    #link ecpense to category/bidirectional
    category=relationship("Category",back_populates="expenses")


#subscription table 
class Subscription(Base):
    __tablename__="subscriptions"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    amount=Column(Integer)
    next_date=Column(Date)


#budget table
class Budget(Base):
    __tablename__="budgets"
    id=Column(Integer, primary_key=True)
    month=Column(String)
    limit=Column(Integer)

#create all tables in database 
Base.metadata.create_all(engine)
#will convert python class into sql tables



#------------------define functions

def add_category():
    name=input("Enter category name: ") #take user input
    session.add(Category(name=name))  #create object and save to db
    session.commit()
    print("category added successfully...")

def add_expense():
    title=input("Enter title: ")
    amount=int(input("enter the amount: "))
    category_id=int(input("category ID: "))

    #create all ojects
    expense=Expense(title=title,amount=amount,date=date.today(),category_id=category_id)
    session.add(expense)
    session.commit()
    print("expense added successfully....")


#will find but id and if not in list then will update it
def update_expense():
    eid=int(input("enter expense ID: "))

    #finf expense by id
    expense=session.query(Expense).filter(Expense.id==eid).first()
    if expense:
        expense.amount=int(input("new amount: "))
        session.commit()
        print("expense updated")
    else:
        print("expense not found")


#will delte
def delete_expense():
    eid=int(input("expense ID: "))
    expense=session.query(Expense).filter(Expense.id==eid).first()
    if expense:
        session.delete(expense)
        session.commit()
        print("expense deleted")
    else:
        print("expense not found")


#search by date
def search_by_date():
    search_date=input("enter the date: ")
    expenses=session.query(Expense).filter(Expense.date==search_date).all()
    for e in expenses:
        print(e.title,"-",e.amount,"-",e.date)


#-------------------------raw sql report
def category_report():
    sql="""
    SELECT categories.name,SUM(expenses.amount)
    FROM categories
    JOIN expenses ON categories.id=expenses.category_id
    GROUP BY categories.name
    """      #inner join / joins actegories and expenses and adds amounts per category gives total spending

    result=session.execute(text(sql))
    print("\n category wise expense report")
    for row in result:
        print(row[0],"=",row[1])


def add_subscription():
    name=input("subscription name: ")
    amount=int(input("subscription amount: "))
    next_date_input=input("next payment date: ")
    next_date=datetime.strptime(next_date_input,"%Y-%m-%d").date()
    session.add(Subscription(name=name,amount=amount,next_date=next_date))
    session.commit()
    print("subscription added...")


def view_subscriptions():
    subs=session.query(Subscription).all()
    print("\nSubscriptions List:")
    for s in subs:
        print(s.id,"-",s.name,"-",s.amount,"- next on:",s.next_date)


def set_budget():
    month=input("enter month: ")
    limit=int(input("montly limit: "))
    session.add(Budget(month=month,limit=limit))
    session.commit()
    print("Budget set...")


def budget_alert():
    month=input("month: ")
    #total budegt raw sql
    total=session.execute(text("SELECT SUM(amount) FROM expenses WHERE date LIKE :m"),{"m": f"{month}%"}).scalar()
    budget=session.query(Budget).filter(Budget.month==month).first()
    if budget and total and total>budget.limit:
        print("budget exceeded")
    else:
        print("in budget")


#-------------- CLI MENU

while True:
    print("""
          ----FINTRACK PRO----
          1.add category
          2.add expense
          3.update expense
          4.delete expense
          5.search expense by date
          6.category expense report
          7.set monthly budget
          8.budget alert
          9.add subscription
          10.view subscriptions
          11.exit
          """ )
    choice=input("choose: ")
    if choice == "1":
        add_category()
    elif choice =="2":
        add_expense()
    elif choice=="3":
        update_expense()
    elif choice=="4":
        delete_expense()
    elif choice=="5":
        search_by_date()
    elif choice=="6":
        category_report()
    elif choice=="7":
        set_budget()
    elif choice=="8":
        budget_alert()
    elif choice=="9":
        add_subscription()
    elif choice=="10":
        view_subscriptions()
    elif choice=="11":
        break
    else:
        print("invalid choice")
    




