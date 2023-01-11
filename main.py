from website import create_app

app = create_app()

# Starts web server if it is explicitly run
if __name__ == '__main__':
    app.run(debug=True)
