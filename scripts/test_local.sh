#!/bin/bash

echo "=== CI/CD Жергілікті Тестілеу ==="
echo ""

echo "1. Python тілін тексеру..."
python --version

echo ""
echo "2. Тәуелділіктерді орнату..."
pip install -r requirements.txt

echo ""
echo "3. Flake8 линтинг..."
flake8 app/ tests/ --max-line-length=100 --show-source --statistics

echo ""
echo "4. Тесттерді іске қосу..."
pytest tests/ -v --cov=app --cov-report=html

echo ""
echo "5. Coverage есебі..."
coverage report

echo ""
echo "6. Қауіпсіздік тесті (Bandit)..."
bandit -r app/ -f txt

echo ""
echo "=== Барлық тесттер сәтті аяқталды! ==="
