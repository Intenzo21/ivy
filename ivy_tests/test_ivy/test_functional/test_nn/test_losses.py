# global
from hypothesis import given, strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_cmd_line_args


# cross_entropy
@handle_cmd_line_args
@given(
    dtype_and_true=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("numeric"),
        min_value=1e-04,
        max_value=1,
        allow_inf=False,
        min_num_dims=1,
        max_num_dims=1,
        min_dim_size=2,
    ),
    dtype_and_pred=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("float"),
        min_value=1e-04,
        max_value=1,
        allow_inf=False,
        exclude_min=True,
        exclude_max=True,
        min_num_dims=1,
        max_num_dims=1,
        min_dim_size=2,
    ),
    reduction=st.sampled_from(["none", "sum", "mean"]),
    axis=helpers.ints(min_value=-1, max_value=0),
    epsilon=helpers.floats(min_value=0, max_value=0.49),
    num_positional_args=helpers.num_positional_args(fn_name="cross_entropy"),
)
def test_cross_entropy(
    dtype_and_true,
    dtype_and_pred,
    reduction,
    axis,
    epsilon,
    as_variable,
    with_out,
    num_positional_args,
    native_array,
    container,
    instance_method,
    fw,
):
    pred_dtype, pred = dtype_and_pred
    true_dtype, true = dtype_and_true

    helpers.test_function(
        input_dtypes=true_dtype + pred_dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        num_positional_args=num_positional_args,
        native_array_flags=native_array,
        container_flags=container,
        instance_method=instance_method,
        fw=fw,
        fn_name="cross_entropy",
        test_gradients=True,
        rtol_=1e-02,
        atol_=1e-02,
        true=true[0],
        pred=pred[0],
        axis=axis,
        epsilon=epsilon,
        reduction=reduction,
    )


# binary_cross_entropy
@handle_cmd_line_args
@given(
    dtype_and_true=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        min_value=0,
        max_value=1,
        allow_inf=False,
        min_num_dims=1,
        max_num_dims=1,
        min_dim_size=2,
    ),
    dtype_and_pred=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("float"),
        min_value=1.0013580322265625e-05,
        max_value=1,
        allow_inf=False,
        exclude_min=True,
        exclude_max=True,
        min_num_dims=1,
        max_num_dims=1,
        min_dim_size=2,
    ),
    reduction=st.sampled_from(["none", "sum", "mean"]),
    epsilon=helpers.floats(min_value=0, max_value=0.49),
    num_positional_args=helpers.num_positional_args(fn_name="binary_cross_entropy"),
)
def test_binary_cross_entropy(
    dtype_and_true,
    dtype_and_pred,
    reduction,
    epsilon,
    as_variable,
    with_out,
    num_positional_args,
    native_array,
    container,
    instance_method,
    fw,
):
    pred_dtype, pred = dtype_and_pred
    true_dtype, true = dtype_and_true
    helpers.test_function(
        input_dtypes=true_dtype + pred_dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        num_positional_args=num_positional_args,
        native_array_flags=native_array,
        container_flags=container,
        instance_method=instance_method,
        fw=fw,
        fn_name="binary_cross_entropy",
        rtol_=1e-1,
        atol_=1e-1,
        true=true[0],
        pred=pred[0],
        epsilon=epsilon,
        reduction=reduction,
    )


# sparse_cross_entropy
@handle_cmd_line_args
@given(
    dtype_and_true=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        min_value=0,
        max_value=2,
        allow_inf=False,
        min_num_dims=1,
        max_num_dims=1,
        min_dim_size=3,
    ),
    dtype_and_pred=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("float"),
        min_value=1.0013580322265625e-05,
        max_value=1,
        allow_inf=False,
        exclude_min=True,
        exclude_max=True,
        min_num_dims=1,
        max_num_dims=1,
        min_dim_size=3,
    ),
    reduction=st.sampled_from(["none", "sum", "mean"]),
    axis=helpers.ints(min_value=-1, max_value=0),
    epsilon=helpers.floats(min_value=0, max_value=0.49),
    num_positional_args=helpers.num_positional_args(fn_name="sparse_cross_entropy"),
)
def test_sparse_cross_entropy(
    dtype_and_true,
    dtype_and_pred,
    reduction,
    axis,
    epsilon,
    as_variable,
    with_out,
    num_positional_args,
    native_array,
    container,
    instance_method,
    fw,
):
    true_dtype, true = dtype_and_true
    pred_dtype, pred = dtype_and_pred
    helpers.test_function(
        input_dtypes=true_dtype + pred_dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        num_positional_args=num_positional_args,
        native_array_flags=native_array,
        container_flags=container,
        instance_method=instance_method,
        fw=fw,
        fn_name="sparse_cross_entropy",
        true=true[0],
        pred=pred[0],
        axis=axis,
        epsilon=epsilon,
        reduction=reduction,
    )
