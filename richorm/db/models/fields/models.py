from .utils import get_default, valueerror
import keyword


class Field:  
    """Base descriptor class for all ORM field types.
    
    Implements the descriptor protocol to manage attribute access
    and provides common functionality for field validation.
    """ 
    def __init__(
        self, 
        max_length=None,
        null:bool = False,
        unique: bool= False,
        default = None,
        primary_key = False,
        db_column = None
    ):
        # Override if primary_key = True
        if primary_key:
            null = False
            default = None
            unique = True
            
        self.primary_key = primary_key
        self.max_length = max_length
        self.null = null
        self.unique = unique
        self.default = default
        self.db_column = db_column
        
        self._validate_attrs()
        valueerror("null",null)
        valueerror("unique",  unique)
        self._validate_db_column_attr()
    
     
    def __set_name__(self, owner, name):
        self.name = name 
        self._check_field_name()
      
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = instance.__dict__.get(self.name)
        if value is None and self.default is not None:
            return get_default(default=self.default)
        
        return value
    
    def  _check_field_name(self):
        """
        Check if field name is valid, i.e. 1) does not end with an
        underscore, 2) does not contain "__" and 3) is not "pk".
        """
        if self.name is None:
            return 
        
        if self.name.endswith("_"):
            raise ValueError(
                f"Field names must not end with an underscore."
            )
        elif "__" in self.name:
            raise ValueError(
                f"Field names must not contain '__'"
            )
        elif self.name == "pk":
            raise ValueError(
                f"'pk' is a reserved word that cannot be used as a field name"
            )
        elif keyword.iskeyword(self.name):
            raise ValueError(
                f"'{self.name}' is a Python keyword and cannot be used as a field name."
            )
        else:
            return
        
    def clean(self,value):
        
        if self.primary_key and value is None :
            raise ValueError(
                f"Primary key field '{self.name}' cannot be null."
            ) 
        
        if value is None and not self.null:
            raise ValueError(
                f"Field '{self.name}' cannot be null."
            )
            
            
    def get_db_column(self):
        if self.db_column is not None:
            return self.db_column
        if not hasattr(self, 'name'):
            raise AttributeError(
                "Field name not yet set. get_db_column() called too early in initialization."
            )
        return self.name
    
    def _validate_db_column_attr(self):
        # Validate db_column type first
        if self.db_column is not None and not isinstance(self.db_column, str):
            raise TypeError(f"db_column must be a string, got {type(self.db_column).__name__}")
        
    def _validate_attrs(self):
        if (
            self.default is not None
            and 
            len(self.default) > self.max_length
        ):
            raise ValueError(
                f"Default value '{self.default}' exceeds max_length "
            )
            

        
class IntegerField(Field):
    """Field that accepts only integer values."""
    
    def __init__(
        self, 
        null:bool=False, 
        unique:bool = False , 
        default = None,
        primary_key = False,
        db_column = None
    ):
        super().__init__(
            null = null, 
            unique=unique, 
            default=default,
            primary_key=primary_key,
            db_column=db_column
        )
    
    def __set__(self, instance, value):
        self.clean(value=value)
        
        if value is None:  
            instance.__dict__[self.name] = None
            return
        
        if not isinstance(value, int):
            raise ValueError(
                f"Expected Integer but got '{value}'."
            )
        
        instance.__dict__[self.name] = value
        
class CharField(Field):
    """Field that accepts string values with optional length constraints."""
    
    def __init__(
        self, 
        max_length = None, 
        null: bool = False , 
        unique:bool = False,
        default = None,
        primary_key = False,
        db_column = None
    ):
        super().__init__(
            max_length=max_length, 
            null=null , 
            unique=unique,
            default=default,
            primary_key=primary_key,
            db_column=db_column
        )
        self._check_max_length_attribute()
        
        
    def __set__(self, instance, value):
        self.clean(value=value)
        
        if value is None:  
            instance.__dict__[self.name] = None
            return
        if not isinstance(value, str):
            raise ValueError(
                f"Expected string but got '{value}'."
            )
        if self.max_length  < len(value):
                raise ValueError(
                    f" Field '{self.name}' exceeds max_length "
                )
            
            
        instance.__dict__[self.name] = value
        
        
    def _check_max_length_attribute(self):
        """Validate that max_length is a positive integer."""
        if self.max_length is None:
            raise TypeError(
                f"CharFields must define a 'max_length' attribute."
            )
            
        if (
            not isinstance(self.max_length, int) 
            or type(self.max_length)==bool 
            or self.max_length <= 0 
        ):
            raise ValueError(
                f"'max_length' must be a positive integer."
            )           
            
    
        
class BooleanField(Field):
    def __init__(
        self, 
        null :bool = False, 
        unique: bool = False,
        default = None,
        primary_key = False,
        db_column = None
    ):
        super().__init__(
            null=null, 
            unique=unique,
            default=default,
            primary_key=primary_key,
            db_column=db_column
        )
        
    def __set__(self, instance , value):
        
        self.clean(value=value)
        
        if value is None:
            instance.__dict__[self.name] = None
            return
        
        true_boolean = self.change_input_to_python_boolean(value)
        instance.__dict__[self.name] = true_boolean
        
    def change_input_to_python_boolean(self, value):
        if self.null and value is None:
            return None
        if value in (True, False):
            # 1/0 are equal to True/False. bool() converts former to latter.
            return bool(value)
        if value in ("t", "True", "1"):
            return True
        if value in ("f", "False", "0"):
            return False
        raise ValueError(
            f"{value} must be either True or False"
        )
             
             
# class EmailField(Field):
#     def __init__(
#         self, 
#         max_length = None, 
#         null: bool = False , 
#         unique:bool = False,
#         default = None,
#         primary_key = False,
#         db_column = None
#     ):
#         super().__init__(
#             max_length=max_length, 
#             null=null , 
#             unique=unique,
#             default=default,
#             primary_key=primary_key,
#             db_column=db_column
#         )
        
#     def __set__(self, instance, value):
        
#         self.clean()
#         if value is None:
#             instance.__dict__[self.name] = None
#             return
        