from main import application


if __name__== "__main__":
    application.run(debug=True)
    # Command to create the database if it doesn't exist
    
    """
    with application.app_context():
        if not os.path.exists('database.db'):  # Check for SQLite file (or adapt for other DBs)
            db.create_all()
            print("Database created successfully!")
    """