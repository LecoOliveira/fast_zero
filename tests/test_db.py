from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='alex',
        password='testando',
        email='arroba@arroba.com'
    )
    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'arroba@arroba.com')
    )

    assert result.username == 'alex'
