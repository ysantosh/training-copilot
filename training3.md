Collecting workspace information
This project is a C#/.NET library management system, organized as a multi-project solution. It provides functionality for managing library patrons, books, loans, and related operations, with a console-based user interface and support for JSON-based data storage.
Key components:
src/Library.ApplicationCore:
Contains core business logic, domain entities (such as Patron, Book, Loan), service interfaces, and enums for operation statuses.
src/Library.Infrastructure:Implements data access using JSON files, with repositories like JsonPatronRepository and JsonLoanRepository, and a JsonData class for loading/saving data.
src/Library.Console:Provides a console application (ConsoleApp) for interacting with the library system, allowing users to search patrons, renew memberships, manage loans, and more.
tests/UnitTests:Contains unit tests for core services using xUnit and NSubstitute, with factories for test data.
Data Storage:Library data (patrons, books, authors, loans, etc.) is stored in JSON files in Json.
Build & CI:Uses .NET 8, with a GitHub Actions workflow (.github/workflows/build-test.yml) for build and test automation.
Main features:
Patron search and detailsMembership renewal with business rulesBook loan management (extend, return)Console-based user interactionJSON-based persistenceThe project is structured for extensibility and testability, separating concerns between core logic, infrastructure, and UI.

