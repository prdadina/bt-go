from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
import random
from datetime import datetime, timedelta
import math

app = Flask(__name__)
CORS(app)


class FinancialReportsService:
    def __init__(self):
        self.historical_data = self.generate_historical_data()
        self.current_year_data = self.generate_current_year_data()
        self.company_metrics = {
            'company_name': 'SC DEMO SRL',
            'founded_year': 2018,
            'sector': 'Tehnologie',
            'employees': 24,
            'current_year': 2024
        }

    def generate_historical_data(self):
        base_year = 2018
        current_year = 2024
        data = {}

        initial_revenue = 800000
        initial_assets = 1200000
        initial_equity = 600000

        for year in range(base_year, current_year + 1):
            years_passed = year - base_year
            growth_factor = 1 + (0.15 + random.uniform(-0.05, 0.08)) ** years_passed

            revenue = int(initial_revenue * growth_factor)
            operating_costs = int(revenue * (0.72 - years_passed * 0.02))
            ebitda = revenue - operating_costs
            depreciation = int(revenue * 0.06)
            interest = int(revenue * 0.02)
            taxes = int((ebitda - depreciation - interest) * 0.16)
            net_profit = ebitda - depreciation - interest - taxes

            total_assets = int(initial_assets * growth_factor * 0.9)
            current_assets = int(total_assets * 0.4)
            total_debt = int(total_assets * (0.5 - years_passed * 0.03))
            equity = int(initial_equity * growth_factor * 1.1)
            current_liabilities = int(total_debt * 0.6)

            debt_to_equity = round(total_debt / equity, 2)
            current_ratio = round(current_assets / current_liabilities, 2)
            roe = round((net_profit / equity) * 100, 1)
            roa = round((net_profit / total_assets) * 100, 1)
            ebitda_margin = round((ebitda / revenue) * 100, 1)

            rating_score = self.calculate_rating_score(debt_to_equity, current_ratio, ebitda_margin, roe)

            data[year] = {
                'year': year,
                'revenue': revenue,
                'operating_costs': operating_costs,
                'ebitda': ebitda,
                'ebitda_margin': ebitda_margin,
                'net_profit': net_profit,
                'total_assets': total_assets,
                'current_assets': current_assets,
                'total_debt': total_debt,
                'equity': equity,
                'current_liabilities': current_liabilities,
                'ratios': {
                    'debt_to_equity': debt_to_equity,
                    'current_ratio': current_ratio,
                    'roe': roe,
                    'roa': roa
                },
                'credit_rating': self.get_rating_from_score(rating_score),
                'rating_score': rating_score
            }

        return data

    def generate_current_year_data(self):
        months = ['Ian', 'Feb', 'Mar', 'Apr', 'Mai', 'Iun', 'Iul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        base_monthly_revenue = 200000
        data = []

        cumulative_revenue = 0
        cumulative_costs = 0
        cumulative_ebitda = 0

        for i, month in enumerate(months):
            seasonal_factor = 1 + 0.2 * math.sin((i * math.pi) / 6)
            monthly_revenue = int(base_monthly_revenue * seasonal_factor * (1 + random.uniform(-0.1, 0.15)))
            monthly_costs = int(monthly_revenue * (0.68 + random.uniform(-0.05, 0.05)))
            monthly_ebitda = monthly_revenue - monthly_costs

            cumulative_revenue += monthly_revenue
            cumulative_costs += monthly_costs
            cumulative_ebitda += monthly_ebitda

            cash_flow = monthly_ebitda + random.randint(-50000, 100000)

            data.append({
                'month': month,
                'month_number': i + 1,
                'revenue': monthly_revenue,
                'operating_costs': monthly_costs,
                'ebitda': monthly_ebitda,
                'cash_flow': cash_flow,
                'cumulative_revenue': cumulative_revenue,
                'cumulative_ebitda': cumulative_ebitda,
                'ebitda_margin': round((monthly_ebitda / monthly_revenue) * 100, 1)
            })

        return data

    def calculate_rating_score(self, debt_to_equity, current_ratio, ebitda_margin, roe):
        score = 0

        if debt_to_equity < 0.3:
            score += 30
        elif debt_to_equity < 0.5:
            score += 25
        elif debt_to_equity < 0.8:
            score += 20
        else:
            score += 10

        if current_ratio > 2.0:
            score += 25
        elif current_ratio > 1.5:
            score += 20
        elif current_ratio > 1.2:
            score += 15
        else:
            score += 5

        if ebitda_margin > 20:
            score += 25
        elif ebitda_margin > 15:
            score += 20
        elif ebitda_margin > 10:
            score += 15
        else:
            score += 5

        if roe > 20:
            score += 20
        elif roe > 15:
            score += 15
        elif roe > 10:
            score += 10
        else:
            score += 5

        return min(score, 100)

    def get_rating_from_score(self, score):
        if score >= 90:
            return {"rating": "AAA", "description": "Excelent", "color": "#10b981"}
        elif score >= 80:
            return {"rating": "AA", "description": "Foarte bun", "color": "#22c55e"}
        elif score >= 70:
            return {"rating": "A", "description": "Bun", "color": "#84cc16"}
        elif score >= 60:
            return {"rating": "BBB", "description": "Acceptabil", "color": "#eab308"}
        elif score >= 50:
            return {"rating": "BB", "description": "Sub medie", "color": "#f97316"}
        else:
            return {"rating": "B", "description": "Risc ridicat", "color": "#ef4444"}

    def get_insights(self):
        current_year = self.historical_data[2024]
        previous_year = self.historical_data[2023]
        company_start = self.historical_data[2018]

        insights = []

        total_growth = round(((current_year['revenue'] - company_start['revenue']) / company_start['revenue']) * 100, 1)
        cagr = round((((current_year['revenue'] / company_start['revenue']) ** (1 / 6)) - 1) * 100, 1)

        insights.append({
            'type': 'growth',
            'title': 'Creștere Istorică',
            'description': f'Compania a crescut cu {total_growth}% de la înființare',
            'metric': f'CAGR: {cagr}%'
        })

        if current_year['ebitda_margin'] > previous_year['ebitda_margin']:
            margin_improvement = round(current_year['ebitda_margin'] - previous_year['ebitda_margin'], 1)
            insights.append({
                'type': 'efficiency',
                'title': 'Îmbunătățire Operațională',
                'description': f'Marja EBITDA a crescut cu {margin_improvement}pp',
                'metric': f'Marja actuală: {current_year["ebitda_margin"]}%'
            })

        if current_year['ratios']['debt_to_equity'] < 0.5:
            insights.append({
                'type': 'stability',
                'title': 'Stabilitate Financiară',
                'description': 'Raport datorii/capitaluri sănătos',
                'metric': f'D/E: {current_year["ratios"]["debt_to_equity"]}'
            })

        rating_improvement = current_year['rating_score'] - company_start['rating_score']
        if rating_improvement > 0:
            insights.append({
                'type': 'rating',
                'title': 'Îmbunătățire Rating',
                'description': f'Scorul de credit a crescut cu {rating_improvement} puncte',
                'metric': f'Rating actual: {current_year["credit_rating"]["rating"]}'
            })

        return insights

    def get_benchmarking(self):
        industry_benchmarks = {
            'tehnologie': {
                'ebitda_margin': {'min': 15, 'avg': 22, 'max': 35},
                'debt_to_equity': {'min': 0.1, 'avg': 0.3, 'max': 0.6},
                'current_ratio': {'min': 1.2, 'avg': 1.8, 'max': 2.5},
                'roe': {'min': 12, 'avg': 18, 'max': 28}
            }
        }

        current_metrics = self.historical_data[2024]
        sector_benchmarks = industry_benchmarks[self.company_metrics['sector'].lower()]

        comparison = {}

        for metric, bounds in sector_benchmarks.items():
            if metric == 'ebitda_margin':
                company_value = current_metrics['ebitda_margin']
            elif metric == 'debt_to_equity':
                company_value = current_metrics['ratios']['debt_to_equity']
            elif metric == 'current_ratio':
                company_value = current_metrics['ratios']['current_ratio']
            elif metric == 'roe':
                company_value = current_metrics['ratios']['roe']

            if company_value >= bounds['avg']:
                performance = 'Above Average'
            elif company_value >= bounds['min']:
                performance = 'Average'
            else:
                performance = 'Below Average'

            comparison[metric] = {
                'company_value': company_value,
                'industry_min': bounds['min'],
                'industry_avg': bounds['avg'],
                'industry_max': bounds['max'],
                'performance': performance
            }

        return {
            'sector': self.company_metrics['sector'],
            'comparison': comparison
        }

    def get_complete_report(self):
        current_data = self.historical_data[2024]
        previous_data = self.historical_data[2023]

        revenue_growth = round(((current_data['revenue'] - previous_data['revenue']) / previous_data['revenue']) * 100,
                               1)
        ebitda_growth = round(((current_data['ebitda'] - previous_data['ebitda']) / previous_data['ebitda']) * 100, 1)

        return {
            'overview': {
                'company_info': self.company_metrics,
                'current_performance': {
                    'revenue': current_data['revenue'],
                    'ebitda': current_data['ebitda'],
                    'ebitda_margin': current_data['ebitda_margin'],
                    'net_profit': current_data['net_profit'],
                    'total_assets': current_data['total_assets'],
                    'equity': current_data['equity'],
                    'credit_rating': current_data['credit_rating']
                },
                'growth_metrics': {
                    'revenue_growth': revenue_growth,
                    'ebitda_growth': ebitda_growth,
                    'rating_trend': 'Îmbunătățire' if current_data['rating_score'] > previous_data[
                        'rating_score'] else 'Stabil'
                }
            },
            'historical': {
                'revenue_trend': [{'year': year, 'value': data['revenue']} for year, data in
                                  self.historical_data.items()],
                'ebitda_trend': [{'year': year, 'value': data['ebitda']} for year, data in
                                 self.historical_data.items()],
                'ebitda_margin_trend': [{'year': year, 'value': data['ebitda_margin']} for year, data in
                                        self.historical_data.items()],
                'rating_trend': [{'year': year, 'value': data['rating_score']} for year, data in
                                 self.historical_data.items()],
                'balance_sheet_evolution': [
                    {
                        'year': year,
                        'assets': data['total_assets'],
                        'debt': data['total_debt'],
                        'equity': data['equity']
                    } for year, data in self.historical_data.items()
                ]
            },
            'current_year': {
                'monthly_performance': {
                    'revenue': [{'month': d['month'], 'value': d['revenue']} for d in self.current_year_data],
                    'ebitda': [{'month': d['month'], 'value': d['ebitda']} for d in self.current_year_data],
                    'cash_flow': [{'month': d['month'], 'value': d['cash_flow']} for d in self.current_year_data]
                },
                'cumulative_trends': [
                    {
                        'month': d['month'],
                        'revenue': d['cumulative_revenue'],
                        'ebitda': d['cumulative_ebitda']
                    } for d in self.current_year_data
                ]
            },
            'insights': self.get_insights(),
            'benchmarking': self.get_benchmarking()
        }


reports_service = FinancialReportsService()


@app.route('/')
def financial_reports():
    return render_template('financial_reports.html')


@app.route('/api/reports/data', methods=['GET'])
def get_reports_data():
    try:
        complete_report = reports_service.get_complete_report()
        return jsonify({
            'success': True,
            'data': complete_report,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/reports/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'online', 'service': 'BT-GO Financial Reports'})


if __name__ == '__main__':
    print("🏦 BT-GO Financial Reports Service Starting...")
    print("📊 Historical Data: 2018-2024")
    print("📈 Monthly Analysis: 2024 breakdown")
    print("🎯 Benchmarking: Industry comparison")
    print("💡 Performance Insights: Automated analysis")
    print("🌐 Server running on http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)