class PCRecord:

    def __init__(self, updated_at, outcome_performance_type, line_description, unique_reference, unit, decimal_places,
                 pcl_actual_pry, pcl_actual_cry, pcl_met, outperformance_or_underperformance_payment,
                 forecast_of_total_2020_25_outperformance_or_underperformance_payment, company_acronym, company_name,
                 year, submission_status, excel_user, excel_file, comment):
        self.updated_at = updated_at
        self.outcome_performance_type = outcome_performance_type
        self.line_description = line_description
        self.unique_reference = unique_reference
        self.unit = unit
        self.decimal_places = decimal_places
        if(None == pcl_actual_pry):
            self.pcl_actual_pry = pcl_actual_pry
        else:
            self.pcl_actual_pry = str(pcl_actual_pry)
        self.pcl_actual_cry = pcl_actual_cry
        self.pcl_met = pcl_met
        self.outperformance_or_underperformance_payment = outperformance_or_underperformance_payment
        self.forecast_of_total_2020_25_outperformance_or_underperformance_payment = forecast_of_total_2020_25_outperformance_or_underperformance_payment
        self.company_acronym = company_acronym
        self.company_name = company_name
        self.year = year
        self.submission_status = submission_status
        self.excel_file = excel_file
        self.excel_user = excel_user
        self.comment = comment
        self.correct_data()

    def print_content(self):
        print("updated_at", "=", self.updated_at)
        print("outcome_performance_type", "=", self.outcome_performance_type)
        print("line_description", "=", self.line_description)
        print("unique_reference", "=", self.unique_reference)
        print("unit", "=", self.unit)
        print("decimal_places", "=", self.decimal_places)
        print("pcl_actual_pry", "=", self.pcl_actual_pry)
        print("pcl_actual_cry", "=", self.pcl_actual_cry)
        print("pcl_met", "=", self.pcl_met)
        print("outperformance_or_underperformance_payment", "=", self.outperformance_or_underperformance_payment)
        print("forecast_of_total_2020_25_outperformance_or_underperformance_payment", "=",
              self.forecast_of_total_2020_25_outperformance_or_underperformance_payment)
        print("company_acronym", "=", self.company_acronym)
        print("company_name", "=", self.company_name)
        print("year", "=", self.year)
        print("submission_status", "=", self.submission_status)
        print("excel_file", "=", self.excel_file)
        print("excel_user", "=", self.excel_user)
        print("comment", "=", self.comment)

    def data_for_db(self):
        basic_tuple = self.updated_at, str(self.excel_file), str(self.excel_user), str(self.comment), 'AMP7', str(self.year), str(self.submission_status), str(self.unique_reference), str(self.company_acronym), str(self.company_name), str(self.pcl_actual_cry), str(self.pcl_met), str(self.outperformance_or_underperformance_payment), str(self.forecast_of_total_2020_25_outperformance_or_underperformance_payment)
        if 'None' in basic_tuple:
            list_of_tuple  = list(basic_tuple)
            new_list_to_supply = []
            for value in list_of_tuple:
                if value == 'None':
                    value = None
                new_list_to_supply.append(value)
            new_tuple = tuple(new_list_to_supply)
            return new_tuple
        else:
            return basic_tuple
        # return self.updated_at, self.excel_file, self.excel_user, self.comment, 'AMP7', self.year, self.submission_status, self.unique_reference, self.company_acronym, self.company_name, self.pcl_actual_cry, self.pcl_met, self.outperformance_or_underperformance_payment, self.forecast_of_total_2020_25_outperformance_or_underperformance_payment

    def correct_data(self):
        if self.pcl_met:
            if self.pcl_met.lower().strip() not in ['yes', 'no', '-', None]:
                print("ERROR - data validation error: ", "pcl_met ", "is |", self.pcl_met,
                      "| This should be Yes, No or -")
        if self.pcl_met == '-':
            self.pcl_met = None
