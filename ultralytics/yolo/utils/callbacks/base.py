def on_pretrain_routine_start(trainer):
    pass


def on_pretrain_routine_end(trainer):
    pass


def on_train_start(trainer):
    pass


def on_train_epoch_start(trainer):
    pass


def on_train_batch_start(trainer):
    pass


def optimizer_step(trainer):
    pass


def on_before_zero_grad(trainer):
    pass


def on_train_batch_end(trainer):
    pass


def on_train_epoch_end(trainer):
    pass


def on_val_start(trainer):
    pass


def on_val_batch_start(trainer):
    pass


def on_val_image_end(trainer):
    pass


def on_val_batch_end(trainer):
    pass


def on_val_end(trainer):
    pass


def on_fit_epoch_end(trainer):
    pass


def on_model_save(trainer):
    pass


def on_train_end(trainer):
    pass


def on_params_update(trainer):
    pass


def teardown(trainer):
    pass


default_callbacks = {
    'on_pretrain_routine_start': on_pretrain_routine_start,
    'on_pretrain_routine_end': on_pretrain_routine_end,
    'on_train_start': on_train_start,
    'on_train_epoch_start': on_train_epoch_start,
    'on_train_batch_start': on_train_batch_start,
    'optimizer_step': optimizer_step,
    'on_before_zero_grad': on_before_zero_grad,
    'on_train_batch_end': on_train_batch_end,
    'on_train_epoch_end': on_train_epoch_end,
    'on_val_start': on_val_start,
    'on_val_batch_start': on_val_batch_start,
    'on_val_image_end': on_val_image_end,
    'on_val_batch_end': on_val_batch_end,
    'on_val_end': on_val_end,
    'on_fit_epoch_end': on_fit_epoch_end,  # fit = train + val
    'on_model_save': on_model_save,
    'on_train_end': on_train_end,
    'on_params_update': on_params_update,
    'teardown': teardown}


def add_integration_callbacks(trainer):
    from .clearml import callbacks as clearml_callbacks
    from .tb import callbacks as tb_callbacks
    from .wb import callbacks as wb_callbacks

    for x in clearml_callbacks, tb_callbacks, wb_callbacks:
        for k, v in x.items():
            trainer.add_callback(k, v)  # add_callback(name, func)