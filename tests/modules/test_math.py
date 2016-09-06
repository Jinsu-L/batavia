from ..utils import ModuleFunctionTestCase, TranspileTestCase

class MathTests(ModuleFunctionTestCase, TranspileTestCase):
    ModuleFunctionTestCase.add_one_arg_tests('math', [
        'acos',
        'acosh',
        'asin',
        'asinh',
        'atan',
        'atanh',
        'ceil',
        'cos',
        'cosh',
        'exp',
        'expm1',
        'floor',
        'log',
        'log10',
        'log1p',
        'log2',
        'sin',
        'sinh',
        'sqrt',
        'tan',
        'tanh',
    ])

    ModuleFunctionTestCase.add_two_arg_tests('math', [
        # 'atan2', # disabled due to the extra time they take on CircleCI for now :(
        # 'log',
        # 'pow',
    ])

    TODO = [
        'copysign',
        'degress',
        'erf',
        'erfc',
        'fabs',
        'factorial',
        'fmod',
        'frexp',
        'fsum',
        'gamma',
        'gcd',
        'hypot',
        'isclose',
        'isfinite',
        'isinf',
        'isnan',
        'ldexp',
        'lgamma',
        'modf',
        'radians',
        'trunc',
    ]


    not_implemented = [
        'test_math_acos_bytearray',
        'test_math_acos_bytes',
        'test_math_acos_class',
        'test_math_acos_complex',
        'test_math_acos_dict',
        'test_math_acos_float',
        'test_math_acos_frozenset',
        'test_math_acos_int',
        'test_math_acos_list',
        'test_math_acos_None',
        'test_math_acos_NotImplemented',
        'test_math_acos_range',
        'test_math_acos_set',
        'test_math_acos_slice',
        'test_math_acos_str',
        'test_math_acos_tuple',

        'test_math_acosh_bool',
        'test_math_acosh_bytearray',
        'test_math_acosh_bytes',
        'test_math_acosh_class',
        'test_math_acosh_complex',
        'test_math_acosh_dict',
        'test_math_acosh_float',
        'test_math_acosh_frozenset',
        'test_math_acosh_int',
        'test_math_acosh_list',
        'test_math_acosh_None',
        'test_math_acosh_NotImplemented',
        'test_math_acosh_range',
        'test_math_acosh_set',
        'test_math_acosh_slice',
        'test_math_acosh_str',
        'test_math_acosh_tuple',

        'test_math_asin_bytearray',
        'test_math_asin_bytes',
        'test_math_asin_class',
        'test_math_asin_complex',
        'test_math_asin_dict',
        'test_math_asin_float',
        'test_math_asin_frozenset',
        'test_math_asin_int',
        'test_math_asin_list',
        'test_math_asin_None',
        'test_math_asin_NotImplemented',
        'test_math_asin_range',
        'test_math_asin_set',
        'test_math_asin_slice',
        'test_math_asin_str',
        'test_math_asin_tuple',

        'test_math_asinh_bool',
        'test_math_asinh_bytearray',
        'test_math_asinh_bytes',
        'test_math_asinh_class',
        'test_math_asinh_complex',
        'test_math_asinh_dict',
        'test_math_asinh_float',
        'test_math_asinh_frozenset',
        'test_math_asinh_int',
        'test_math_asinh_list',
        'test_math_asinh_None',
        'test_math_asinh_NotImplemented',
        'test_math_asinh_range',
        'test_math_asinh_set',
        'test_math_asinh_slice',
        'test_math_asinh_str',
        'test_math_asinh_tuple',

        'test_math_atan2_bool_frozenset',
        'test_math_atan2_bytearray_frozenset',
        'test_math_atan2_bytes_frozenset',
        'test_math_atan2_class_frozenset',
        'test_math_atan2_complex_frozenset',
        'test_math_atan2_dict_frozenset',
        'test_math_atan2_float_frozenset',
        'test_math_atan2_frozenset_bool',
        'test_math_atan2_frozenset_bytearray',
        'test_math_atan2_frozenset_bytes',
        'test_math_atan2_frozenset_class',
        'test_math_atan2_frozenset_complex',
        'test_math_atan2_frozenset_dict',
        'test_math_atan2_frozenset_float',
        'test_math_atan2_frozenset_frozenset',
        'test_math_atan2_frozenset_int',
        'test_math_atan2_frozenset_list',
        'test_math_atan2_frozenset_None',
        'test_math_atan2_frozenset_NotImplemented',
        'test_math_atan2_frozenset_range',
        'test_math_atan2_frozenset_set',
        'test_math_atan2_frozenset_slice',
        'test_math_atan2_frozenset_str',
        'test_math_atan2_frozenset_tuple',
        'test_math_atan2_int_frozenset',
        'test_math_atan2_int_int',
        'test_math_atan2_list_frozenset',
        'test_math_atan2_None_frozenset',
        'test_math_atan2_NotImplemented_frozenset',
        'test_math_atan2_range_frozenset',
        'test_math_atan2_set_frozenset',
        'test_math_atan2_slice_frozenset',
        'test_math_atan2_str_frozenset',
        'test_math_atan2_tuple_frozenset',

        'test_math_atan_frozenset',

        'test_math_atanh_frozenset',

        'test_math_ceil_frozenset',

        'test_math_cos_frozenset',

        'test_math_cosh_frozenset',

        'test_math_exp_frozenset',

        'test_math_expm1_frozenset',

        'test_math_floor_frozenset',

        'test_math_log_bool',
        'test_math_log_bool_frozenset',
        'test_math_log_bytearray_frozenset',
        'test_math_log_bytes_frozenset',
        'test_math_log_class_frozenset',
        'test_math_log_complex_frozenset',
        'test_math_log_dict_frozenset',
        'test_math_log_float',
        'test_math_log_float_frozenset',
        'test_math_log_frozenset',
        'test_math_log_frozenset_bool',
        'test_math_log_frozenset_bytearray',
        'test_math_log_frozenset_bytes',
        'test_math_log_frozenset_class',
        'test_math_log_frozenset_complex',
        'test_math_log_frozenset_dict',
        'test_math_log_frozenset_float',
        'test_math_log_frozenset_frozenset',
        'test_math_log_frozenset_int',
        'test_math_log_frozenset_list',
        'test_math_log_frozenset_None',
        'test_math_log_frozenset_NotImplemented',
        'test_math_log_frozenset_range',
        'test_math_log_frozenset_set',
        'test_math_log_frozenset_slice',
        'test_math_log_frozenset_str',
        'test_math_log_frozenset_tuple',
        'test_math_log_int',
        'test_math_log_int_int',
        'test_math_log_int_frozenset',
        'test_math_log_list_frozenset',
        'test_math_log_None_frozenset',
        'test_math_log_NotImplemented_frozenset',
        'test_math_log_range_frozenset',
        'test_math_log_set_frozenset',
        'test_math_log_slice_frozenset',
        'test_math_log_str_frozenset',
        'test_math_log_tuple_frozenset',

        'test_math_log10_bool',
        'test_math_log10_bytearray',
        'test_math_log10_bytes',
        'test_math_log10_class',
        'test_math_log10_complex',
        'test_math_log10_dict',
        'test_math_log10_float',
        'test_math_log10_frozenset',
        'test_math_log10_int',
        'test_math_log10_list',
        'test_math_log10_None',
        'test_math_log10_NotImplemented',
        'test_math_log10_range',
        'test_math_log10_set',
        'test_math_log10_slice',
        'test_math_log10_str',
        'test_math_log10_tuple',

        'test_math_log1p_bytearray',
        'test_math_log1p_bytes',
        'test_math_log1p_class',
        'test_math_log1p_complex',
        'test_math_log1p_dict',
        'test_math_log1p_float',
        'test_math_log1p_frozenset',
        'test_math_log1p_int',
        'test_math_log1p_list',
        'test_math_log1p_None',
        'test_math_log1p_NotImplemented',
        'test_math_log1p_range',
        'test_math_log1p_set',
        'test_math_log1p_slice',
        'test_math_log1p_str',
        'test_math_log1p_tuple',

        'test_math_log2_bool',
        'test_math_log2_bytearray',
        'test_math_log2_bytes',
        'test_math_log2_class',
        'test_math_log2_complex',
        'test_math_log2_dict',
        'test_math_log2_float',
        'test_math_log2_frozenset',
        'test_math_log2_int',
        'test_math_log2_list',
        'test_math_log2_None',
        'test_math_log2_NotImplemented',
        'test_math_log2_range',
        'test_math_log2_set',
        'test_math_log2_slice',
        'test_math_log2_str',
        'test_math_log2_tuple',

        'test_math_pow_bool_frozenset',
        'test_math_pow_bytearray_frozenset',
        'test_math_pow_bytes_frozenset',
        'test_math_pow_class_frozenset',
        'test_math_pow_complex_frozenset',
        'test_math_pow_dict_frozenset',
        'test_math_pow_float_frozenset',
        'test_math_pow_frozenset_bool',
        'test_math_pow_frozenset_bytearray',
        'test_math_pow_frozenset_bytes',
        'test_math_pow_frozenset_class',
        'test_math_pow_frozenset_complex',
        'test_math_pow_frozenset_dict',
        'test_math_pow_frozenset_float',
        'test_math_pow_frozenset_frozenset',
        'test_math_pow_frozenset_int',
        'test_math_pow_frozenset_list',
        'test_math_pow_frozenset_None',
        'test_math_pow_frozenset_NotImplemented',
        'test_math_pow_frozenset_range',
        'test_math_pow_frozenset_set',
        'test_math_pow_frozenset_slice',
        'test_math_pow_frozenset_str',
        'test_math_pow_frozenset_tuple',
        'test_math_pow_int_frozenset',
        'test_math_pow_int_int',
        'test_math_pow_list_frozenset',
        'test_math_pow_None_frozenset',
        'test_math_pow_NotImplemented_frozenset',
        'test_math_pow_range_frozenset',
        'test_math_pow_set_frozenset',
        'test_math_pow_slice_frozenset',
        'test_math_pow_str_frozenset',
        'test_math_pow_tuple_frozenset',

        'test_math_sin_frozenset',

        'test_math_sinh_frozenset',

        'test_math_sqrt_float',
        'test_math_sqrt_frozenset',
        'test_math_sqrt_int',

        'test_math_tan_frozenset',

        'test_math_tan_frozenset',
    ]

    def test_constants(self):
        self.assertCodeExecution("""
            import math
            print(math.e)
            print(math.inf)
            print(math.nan)
            print(math.pi)
            """)
