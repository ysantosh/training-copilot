# This code defines a function to validate email addresses using regular expressions.
Converted in C#

using System;
using System.Text.RegularExpressions;

class Program
{
    static bool IsValidEmail(string email)
    {
        // Checks if the provided email address is valid based on a regular expression pattern.
        string pattern = @"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$";
        return Regex.IsMatch(email, pattern);
    }

    static void Main(string[] args)
    {
        Console.Write("Enter an email address: ");
        string email = Console.ReadLine();
        if (IsValidEmail(email))
        {
            Console.WriteLine("Valid email address.");
        }
        else
        {
            Console.WriteLine("Invalid email address.");
        }
    }
}