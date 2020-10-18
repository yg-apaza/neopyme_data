class Evaluate:
    def __init__(taxpayer_id, persona1_type_x, personal_id, customer_id, sbs_customer_id, segmento, admission_date, spanish_sector_company_name, employees_number, branches_number, activity_start_date, seniority_company_years_number, company_size_desc, foreign_company_mark_type, department_name, province_name, district_name, private_1_mark_desc, market_share_per, ranking_number, min_usd_billing_amount, max_usd_billing_amount, min_pen_billing_amount, max_pen_billing_amount, income_amount, net_profit_amount, assets_amount, equity_amount, liabilities_amount, usd_export, usd_import_amount, state_sales_amount, roe_per, pbi_sector_per, personal_type_y, personal_id_x_x, taxpayer_start_date_x, taxpayer_end_date_x, comm_start_date_x, company_economic_activity_id_y):
        self.taxpayer_id = taxpayer_id
        self.persona1_type_x = persona1_type_x
        self.personal_id = personal_id
        self.customer_id = customer_id
        self.sbs_customer_id = sbs_customer_id
        self.segmento = segmento
        self.admission_date = admission_date
        self.spanish_sector_company_name = spanish_sector_company_name
        self.employees_number = employees_number
        self.branches_number = branches_number
        self.activity_start_date = activity_start_date
        self.seniority_company_years_number = seniority_company_years_number
        self.company_size_desc = company_size_desc
        self.foreign_company_mark_type = foreign_company_mark_type
        self.department_name = department_name
        self.province_name = province_name
        self.district_name = district_name
        self.private_1_mark_desc = private_1_mark_desc
        self.market_share_per = market_share_per
        self.ranking_number = ranking_number
        self.min_usd_billing_amount = min_usd_billing_amount
        self.max_usd_billing_amount = max_usd_billing_amount
        self.min_pen_billing_amount = min_pen_billing_amount
        self.max_pen_billing_amount = max_pen_billing_amount
        self.income_amount = income_amount
        self.net_profit_amount = net_profit_amount
        self.assets_amount = assets_amount
        self.equity_amount = equity_amount
        self.liabilities_amount = liabilities_amount
        self.usd_export = usd_export
        self.usd_import_amount = usd_import_amount
        self.state_sales_amount = state_sales_amount
        self.roe_per = roe_per
        self.pbi_sector_per = pbi_sector_per
        self.personal_type_y = personal_type_y
        self.personal_id_x_x = personal_id_x_x
        self.taxpayer_start_date_x = taxpayer_start_date_x
        self.taxpayer_end_date_x = taxpayer_end_date_x
        self.comm_start_date_x = comm_start_date_x
        self.company_economic_activity_id_y = company_economic_activity_id_y

    def evaluate(self):
        # employees_number
        safe = 1
        emp = employees_number/100
        safe = safe*emp

        # branches_number
        safe = safe + branches_number/100

        # activity_start_date
        safe = safe + (1990-activity_start_date)/100

        #company_size_desc
        safe = safe + company_size_desc/10

        if ranking_number > 100:
            safe = safe+0.1
        if min_usd_billing_amount > 100:
            safe = safe+0.1
        if max_usd_billing_amount > 100:
            safe = safe+0.1
        if min_pen_billing_amount > 100:
            safe = safe+0.1
        if max_pen_billing_amount > 100:
            safe = safe+0.1
        if income_amount > 100:
            safe = safe+0.1
        if net_profit_amount > 100:
            safe = safe+0.1
        if assets_amount > 100:
            safe = safe+0.1
        if equity_amount > 100:
            safe = safe+0.1
        if liabilities_amount > 100:
            safe = safe+0.1
        if usd_export > 0:
            safe = safe+0.1
        if usd_import_amount > 100:
            safe = safe+0.1
        if state_sales_amount > 100:
            safe = safe+0.1
        if roe_per > 100:
            safe = safe+0.1
        if pbi_sector_per > 100:
            safe = safe+0.5
        
        if safe > 90 :
            return 1
        else: return 0