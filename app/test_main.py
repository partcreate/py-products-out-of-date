import pytest
import datetime
from _pytest.monkeypatch import MonkeyPatch

from app import main
from app.main import outdated_products


@pytest.mark.parametrize(
    "product, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2025, 10, 4),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2025, 10, 5),
                    "price": 160
                }
            ],
            [
                "salmon",
                "chicken"
            ]
        )
    ]
)
def test_outdated_products(
        monkeypatch: MonkeyPatch,
        product: list,
        expected: list

) -> None:
    monkeypatch.setattr(
        main, "outdated_products", outdated_products
    )

    assert outdated_products(product) == expected
