def main():
    num_males = int(input("Enter the number of males: "))
    num_females = int(input("Enter the number of females: "))

    total_students = num_males + num_females

    m_perc = (num_males / total_students) * 100
    f_perc = (num_females / total_students) * 100

    print("The total number of students:", total_students)
    print("The number of males and females:", num_males, "and", num_females)
    print(f"The percentage of males and females: {m_perc:.2f}% and {f_perc:.2f}%")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
