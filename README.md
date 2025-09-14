# AI-Career-Advisor
This is a simple, two-part application for a digital wallet. It consists of a Java back-end service that handles the core financial logic and a front-end web application built with HTML, CSS (using Tailwind CSS), and JavaScript for user interaction.

Features
 * User Management: Create and manage user accounts with an initial balance.
 * Balance Inquiry: Check the current balance of any user's wallet.
 * Fund Transfer: Securely transfer funds from one user to another.
 * Deposits & Withdrawals: Simulate deposits and withdrawals to/from user accounts.

Technology Stack
 * Back-end: Java
   * Simulates a back-end service with in-memory data structures (HashMap) for    demonstration purposes.
   * Includes core business logic for financial transactions.
 * Front-end: HTML, CSS, JavaScript
   * HTML: The structure of the web application.
   * Tailwind CSS: A utility-first CSS framework for rapid and responsive styling.
   * JavaScript: Handles front-end logic, form submissions, and makes simulated API calls to the back-end.

How to Run

Back-end (Java)
The DigitalWalletService.java file is a standalone Java class that contains a main method for testing the core logic. To run the back-end:
   1. Compile the Java file:
        javac DigitalWalletService.java
   2. Run the compiled class:
        java DigitalWalletService
        The console will show the simulated transactions and balance updates.

Front-end (Web App)
The BankingWebApp.html file is a single-file web application. It does not require a local server to run and can be opened directly in a web browser.

 1. Open the BankingWebApp.html file in your preferred web browser (e.g., Chrome, Firefox, Safari).
 2. The application will display a simple dashboard and a form for sending money.
 3. Note: The front-end is currently a proof-of-concept and uses placeholder logic. The JavaScript fetch calls are directed to a placeholder URL (http://your-java-backend-api.com) and do not actually connect to the provided Java service. For a fully functional application, you would need to set up a real back-end API that exposes endpoints for the front-end to call.
