import os
import argparse
from solver import Solver
from data_loader import get_loader
from torch.backends import cudnn

def str2bool(v):
    return v.lower() in ('true')

def main(config):
    # For fast training.
    cudnn.benchmark = True

    # Create directories if they do not exist.
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)
    if not os.path.exists(config.model_save_dir):
        os.makedirs(config.model_save_dir)
    if not os.path.exists(config.sample_dir):
        os.makedirs(config.sample_dir)
    if not os.path.exists(config.result_dir):
        os.makedirs(config.result_dir)

    # Data loader to preprocess images.
    celeba_loader = get_loader(config.celeba_image_dir, config.attr_path, config.selected_attrs,
                                config.celeba_crop_size, config.image_size, config.batch_size,
                                'CelebA', config.mode, config.num_workers)

    # Solver for training and testing StarGAN.
    solver = Solver(celeba_loader, config)
    if config.mode == 'train':
        solver.train()
    elif config.mode == 'test':
        solver.test()

#all possible command line options
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    iterations = 21000
    # Model configuration.
    parser.add_argument('--c_dim', type=int, default=4, help='dimension of domain labels (1st dataset)')
    parser.add_argument('--celeba_crop_size', type=int, default=178, help='crop size for the CelebA dataset')
    parser.add_argument('--image_size', type=int, default=128, help='image resolution')
    parser.add_argument('--g_conv_dim', type=int, default=64, help='number of conv filters in the first layer of G')
    parser.add_argument('--d_conv_dim', type=int, default=64, help='number of conv filters in the first layer of D')
    parser.add_argument('--g_repeat_num', type=int, default=6, help='number of residual blocks in G')
    parser.add_argument('--d_repeat_num', type=int, default=6, help='number of strided conv layers in D')
    parser.add_argument('--lambda_cls', type=float, default=1, help='weight for domain classification loss')
    parser.add_argument('--lambda_rec', type=float, default=10, help='weight for reconstruction loss')
    parser.add_argument('--lambda_gp', type=float, default=10, help='weight for gradient penalty')
    
    # Training configuration.
    parser.add_argument('--dataset', type=str, default='CelebA', help='name of dataset to use')
    parser.add_argument('--batch_size', type=int, default=16, help='mini-batch size')
    parser.add_argument('--num_iters', type=int, default=iterations, help='number of total iterations for training D')
    parser.add_argument('--num_iters_decay', type=int, default=10000, help='number of iterations for decaying lr')
    parser.add_argument('--g_lr', type=float, default=0.0001, help='learning rate for G')
    parser.add_argument('--d_lr', type=float, default=0.0001, help='learning rate for D')
    parser.add_argument('--n_critic', type=int, default=5, help='number of D updates per each G update')
    parser.add_argument('--beta1', type=float, default=0.5, help='beta1 for Adam optimizer')
    parser.add_argument('--beta2', type=float, default=0.999, help='beta2 for Adam optimizer')
    parser.add_argument('--resume_iters', type=int, default=None, help='resume training from this step')
    parser.add_argument('--selected_attrs', '--list', nargs='+', help='selected attributes for the CelebA dataset',
                        default=['Male', 'Young','Double_Chin','Pointy_Nose'])

    # Test configuration.
    parser.add_argument('--test_iters', type=int, default=iterations, help='test model from this step')

    # Miscellaneous.
    parser.add_argument('--num_workers', type=int, default=1)
    parser.add_argument('--mode', type=str, default='train', choices=['train', 'test'])

    # Directories.
    parser.add_argument('--celeba_image_dir', type=str, default='data/celeba/images')
    parser.add_argument('--attr_path', type=str, default='data/celeba/list_attr_celeba.txt')
    parser.add_argument('--log_dir', type=str, default='stargan_celeba/logs')
    parser.add_argument('--model_save_dir', type=str, default='stargan_celeba/models')
    parser.add_argument('--sample_dir', type=str, default='stargan_celeba/samples')
    parser.add_argument('--result_dir', type=str, default='stargan_celeba/results')

    # Step size.
    parser.add_argument('--log_step', type=int, default=1)
    parser.add_argument('--sample_step', type=int, default=1000)
    parser.add_argument('--model_save_step', type=int, default=1000)
    parser.add_argument('--lr_update_step', type=int, default=1000)

    config = parser.parse_args()
    print(config)
    main(config)