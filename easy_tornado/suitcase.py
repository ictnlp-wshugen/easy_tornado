# -*- coding: utf-8 -*-
# author: 王树根
# email: wsg1107556314@163.com
# date: 2025/12/16 23:03


def add_criteria_argument(parser):
  parser.add_argument(
    '--criteria', '-c', action='append', default=[],
    help='criteria to eval, if not True then filter out, "obj" is the dict'
  )
  parser.add_argument(
    '--silent', '-s', action='store_true', default=False,
    help='silent mode for less output'
  )


def get_criteria_arguments(args):
  return args.criteria, args.silent


def add_io_arguments(parser, multi_input=False, output_dir=False):
  input_parser = parser.add_mutually_exclusive_group(required=True)
  input_parser.add_argument(
    '--mapreduce', '-mr', action='store_true', default=False,
    help='read and write in mapreduce procedure manner'
  )
  if multi_input:
    input_parser.add_argument(
      '--input-paths', '-i', action='append', default=[],
      help='paths to input file'
    )
  else:
    input_parser.add_argument(
      '--input-path', '-i', default=None,
      help='path to input file'
    )
  add_criteria_argument(parser)
  parser.add_argument(
    '--dry-run', '-dr', action='store_true', default=False,
    help='test data loader and do not execute'
  )
  parser.add_argument(
    '--json-pro', '-jp', action='store_true', default=False,
    help='use jsonlines to load lines instead of load_file_contents'
  )
  if output_dir:
    parser.add_argument(
      '--output-dir', '-o', default=None,
      help='path to output results files under this directory'
    )
  else:
    parser.add_argument(
      '--output-path', '-o', default=None,
      help='path to output results file'
    )
  parser.add_argument(
    '--remove-if-exists', '-rie', action='store_true', default=False,
    help='remove output path if already exists'
  )
  return input_parser


def get_in_arguments(args, multi_input=False):
  return args.mapreduce, args.input_paths if multi_input else args.input_path


def get_json_arguments(args):
  return args.json_pro, args.dry_run


def get_out_arguments(args, output_dir=False):
  output_val = args.output_dir if output_dir else args.output_path
  return output_val, args.remove_if_exists


def add_qps_argument(parser):
  parser.add_argument(
    '--query-per-second', '-qps', type=int, default=2,
    help='request/invoke speed limit'
  )
  parser.add_argument(
    '--timeout', '-to', type=int, default=3600,
    help='request/invoke timeout seconds'
  )
  parser.add_argument(
    '--patience', '-rp', type=int, default=3,
    help='max retry times before give up'
  )
  parser.add_argument(
    '--cooldown', '-cd', type=int, default=0.3,
    help='cooldown time (second) before next try'
  )


def get_qps_arguments(args):
  return args.query_per_second, args.timeout, args.patience, args.cooldown


def add_ckpt_argument(parser):
  parser.add_argument(
    '--keep-as-key', '-kak', default=None,
    help='KEEP request/invoke result as an attribute'
  )
  parser.add_argument(
    '--write-interval', '-wi', type=int, default=10,
    help='save interval: per number of lines'
  )


def get_ckpt_arguments(args):
  return args.keep_as_key, args.write_interval


def add_multirun_args(parser):
  parser.add_argument(
    '--world-rank', type=int, metavar='N', default=None,
    help='multi process running index order'
  )
  parser.add_argument(
    '--local-size', type=int, metavar='N', default=None,
    help='multi process running local size'
  )


def get_multirun_arguments(args):
  return args.world_rank, args.local_size
