using System;

class Program
{
    static void Main()
    {
        double percentage = double.Parse(Console.ReadLine());
        double price = double.Parse(Console.ReadLine());
        double discount = (percentage*price)/100.0;
        double discountPrice = price-discount;
        Console.WriteLine($"discounted price in lv : {discountPrice}, discount amount in lv : {discount}");

    }
    static void Main1()
    {
        Console.WriteLine("enter the day hour:");
        double hour = double.Parse(Console.ReadLine());
        if (hour <= 12 and hour >= 6)
        {
           Console.WriteLine($"good morning darling, have you slept well ?");
        }
        else if(hour <= 16)
        {
            Console.WriteLine("good afternoon");

        }
        else if(hour<=21)
        {
             Console.WriteLine("good evening");

        }
        else
        {
            Console.WriteLine("good night and rest for next battle");

        }
   
    
   
        
        

    }

}


