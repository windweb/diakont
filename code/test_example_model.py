import pytest
from PyQt5.QtCore import QModelIndex, Qt
from example_model import ExampleModel
# from .example_widget import ExampleModel

@pytest.fixture
def example_model():
    model = ExampleModel()
    return model

def test_model_initialization(example_model):
    # Проверяем, что модель инициализируется с базовыми значениями
    assert example_model is not None
    assert example_model.rowCount(QModelIndex()) == 1  # Проверяем, что есть один корневой элемент

def test_model_data(example_model):
    # Проверяем, что данные корректно возвращаются из модели
    index = example_model.index(0, 1, QModelIndex())  # Получаем индекс первого элемента
    assert example_model.data(index, Qt.DisplayRole) == 0  # Проверяем значение по умолчанию для "Times"

def test_model_set_data(example_model):    # Проверяем, что данные могут быть изменены
    index = example_model.index(0, 1, QModelIndex())  # Получаем индекс первого элемента
    example_model.setData(index, 5, Qt.EditRole)  # Устанавливаем новое значение для "Times"
    assert example_model.data(index, Qt.DisplayRole) == 5  # Проверяем, что значение изменилось

def test_set_trigger(example_model, mocker):
    # Проверяем, что метод set_trigger вызывает make_request с правильными аргументами
    mocker.patch.object(example_model, 'make_request')
    example_model.set_trigger(get_data=True)
    expected_request = example_model.make_command(
        RequestTypes.SCOPE, "", ScopeMethods.REQUEST, example_model.to_json()[0]
    )
    example_model.make_request.assert_called_once_with(expected_request)

def test_reset_trigger(example_model, mocker):
    # Проверяем, что метод reset_trigger вызывает make_request с правильными аргументами
    mocker.patch.object(example_model, 'make_request')
    example_model.reset_trigger()
    expected_request = example_model.make_command(
        RequestTypes.SCOPE, "", ScopeMethods.RESET
    )
    example_model.make_request.assert_called_once_with(expected_request)

def test_get_data(example_model, mocker):
    # Проверяем, что метод get_data вызывает make_request с правильными аргументами
    mocker.patch.object(example_model, 'make_request')
    example_model.get_data()
    expected_request = example_model.make_command(
        RequestTypes.SCOPE, "", ScopeMethods.DOWNLOAD
    )
    example_model.make_request.assert_called_once_with(expected_request)