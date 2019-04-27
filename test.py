from app import app



try:
    app.run(host="localhost", port=1337, debug=True)
except Exception as e:
    print(f"The issue was: {e}. Try to debug your code and do it again")