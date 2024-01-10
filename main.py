# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def ingest_file(file_name):
    df = pd.read_csv(file_name)
    return df

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import collections
    df = ingest_file("gsearch_jobs.csv")
    df = df.drop(['Unnamed: 0', 'index', 'description', 'extensions', 'job_id', 'thumbnail', 'posted_at', 'search_term', 'search_location', 'commute_time'], axis=1)
    df['Grouped Values'] = df['title'].str.lower().apply(lambda x: 'Data Analyst' if 'data analyst' in x else
                                                    'Data Engineer' if 'data engineer' in x else
                                                    'Data Scientist' if 'data scientist' in x else
                                                    'Business Analyst' if ('business analyst' in x or 'bi analyst' in x) else
                                                    'Business Intelligence Analyst' if 'business intelligence analyst' in x else
                                                    'Software Engineer' if 'software engineer' in x else
                                                    'Manager' if 'manager' in x else
                                                    'Consultant' if 'consultant' in x else
                                                    'Director' if 'director' in x else
                                                    'others')

    # Convert Empty values from work_from_home column to False
    df.work_from_home = df.work_from_home.fillna('False')

    #Returns two list of values containing the unique key and the unique count
    # df['description_tokens'] = df['description_tokens'].apply(eval)
    #
    # counts = {}
    #
    # for lst in df['description_tokens']:
    #     for item in set(lst):
    #         counts[item] = counts.get(item,0) + 1
    #
    # sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    #
    # all_unique_values = [item[0] for item in sorted_counts]
    # all_counts = [item[1] for item in sorted_counts]
    # print("Unique Values: ", all_unique_values)
    # print("Counts: ", all_counts)
    df.to_csv(r"output.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
