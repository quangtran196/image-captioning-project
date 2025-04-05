"""
Default configuration for the image captioning model
"""

# Data settings
DATA_CONFIG = {
    'coco_path': 'data/coco',
    'batch_size': 32,
    'num_workers': 4,
    'crop_size': 224,
    'min_word_freq': 5,
    'captions_per_image': 5,
    'max_len': 50,
}

# Model settings
MODEL_CONFIG = {
    # Encoder (ResNet-101)
    'encoded_image_size': 14,
    'fine_tune_encoder': True,
    'encoder_lr': 1e-4,
    
    # Decoder (LSTM)
    'embed_dim': 300,
    'attention_dim': 512,
    'decoder_dim': 512, 
    'dropout': 0.5,
    'decoder_lr': 4e-4,
    
    # Transformer Decoder
    'transformer_embed_dim': 512,
    'transformer_num_heads': 8,
    'transformer_ff_dim': 2048,
    'transformer_num_layers': 6,
}

# Training settings
TRAIN_CONFIG = {
    'num_epochs': 20,
    'grad_clip': 5.0,
    'alpha_c': 1.0,  # Attention regularization parameter
    'print_freq': 100,
    'save_freq': 1,
    'beam_size': 5,
    'checkpoint_path': 'checkpoints',
    'best_model_path': 'checkpoints/best_model',
    'workers': 4,
}

# Experiment tracking
EXPERIMENT_CONFIG = {
    'wandb_project': 'image_captioning',
    'use_tensorboard': True,
    'log_dir': 'logs',
}