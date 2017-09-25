{
    'variables': {
        #'library': 'static_library',
        'library' : 'shared_library',
    },
    'target_defaults': {
		'win_delay_load_hook': 'false',
		'msvs_settings': {
			# This magical incantation is necessary because VC++ will compile
			# object files to same directory... even if they have the same name!
			'VCCLCompilerTool': {
			  'ObjectFile': '$(IntDir)/%(RelativeDir)/',
			  #'AdditionalOptions': [ '/EHsc', '/wd4244']
			  'WarningLevel': 0,
			  'WholeProgramOptimization': 'false',
			  'AdditionalOptions': ['/EHsc'],
			  'ExceptionHandling' : 1, #/EHsc
			},
			
		},
		'configurations':{
			'Debug':{
				'conditions': [
				  ['target_arch=="x64"', {
					'msvs_configuration_platform': 'x64',
				  }],
				  ['1==1',{

					'defines':[
						'DEBUG',
					],
					'msvs_settings': {		
						'VCCLCompilerTool': {
						  #'WholeProgramOptimization' : 'false',
						  #'AdditionalOptions': ['/GL-','/w'], #['/wd4244' ,'/wd4018','/wd4133' ,'/wd4090'] #GL- was added because the forced optimization coming from node-gyp is disturbing the weird coding style from ffmpeg.
						  'WarningLevel': 0,
						  'WholeProgramOptimization': 'false',
						  'AdditionalOptions': ['/EHsc'],
						  'ExceptionHandling' : 1, #/EHsc
						  'RuntimeLibrary': 3, # dll debug
						},
						'VCLinkerTool' : {
							'GenerateDebugInformation' : 'true',
							'conditions':[
								['target_arch=="x64"', {
									'TargetMachine' : 17 # /MACHINE:X64
								}],
							],
							
						}
					}
				
				  }],
				],
				
			},
			'Release':{
				'conditions': [
				  ['target_arch=="x64"', {
					'msvs_configuration_platform': 'x64',
				  }],
				],
				'msvs_settings': {			
					'VCCLCompilerTool': {
						'WholeProgramOptimization' : 'false',
						#'AdditionalOptions': ['/GL-','/w'], #['/wd4244' ,'/wd4018','/wd4133' ,'/wd4090'] #GL- was added because the forced optimization coming from node-gyp is disturbing the weird coding style from ffmpeg.
						'WarningLevel': 0,
						  'WholeProgramOptimization': 'false',
						  'AdditionalOptions': ['/EHsc'],
						  'ExceptionHandling' : 1, #/EHsc
						  'RuntimeLibrary': 2, # dll release
					},
					'VCLinkerTool' : {
						'conditions':[
							['target_arch=="x64"', {
								'TargetMachine' : 17 # /MACHINE:X64
							}],
						],
						
					}
				}
			},
		},
		
		'conditions': [
			['OS == "win"',{
				'defines':[
                    'WIN32',
					'DELAYIMP_INSECURE_WRITABLE_HOOKS'
				],
			}],
		  ['OS != "win"', {
			'defines': [
			  '_LARGEFILE_SOURCE',
			  '_FILE_OFFSET_BITS=64',
			  
			],
			'cflags':[
				'-fPIC',
				'-fexceptions',
			],
			'cflags!': [ '-fno-exceptions' ],
			'cflags_cc!': [ '-fno-exceptions' ],
			'conditions': [
				['OS=="mac"', {
				  'xcode_settings': {
					'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
				  }
				}]
			],
			'conditions': [
			  ['OS=="solaris"', {
				'cflags': [ '-pthreads' ],
			  }],
			  ['OS not in "solaris android"', {
				'cflags': [ '-pthread' ],
			  }],
			],
		}],
		['OS=="android"',{
			'defines':[
				'ANDROID'
			],
		  }],
		],
	  },

    "targets": [
        {
            'target_name': 'apr',
            'type': '<(library)',
            'dependencies': [
                '../libexpat.module/libexpat.gyp:libexpat'
            ],
            'include_dirs':[
                "src/include",
                "src/include/private",
                
                "config",
                "config/<(OS)",
                "config/<(OS)/<(target_arch)",
            ],
            "defines":[
                #'APR_DECLARE_STATIC',
                'APR_DECLARE_EXPORT',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    "src/include",

                    "config",
                    "config/<(OS)",
                    "config/<(OS)/<(target_arch)",
                ],
                "defines":[
                ],
            },
            'conditions':[
                ['OS == "linux"',{
                    'include_dirs':[
                        "src/include/arch/unix",
                    ],
                    'direct_dependent_settings': {
                        'include_dirs': [
                            "src/include/arch/unix",
                        ]
                    },
                    'sources':[
                        "src/shmem/unix",
                        "src/shmem/unix/shm.c",
                        "src/misc/unix",
                        "src/misc/unix/start.c",
                        "src/misc/unix/errorcodes.c",
                        "src/misc/unix/otherchild.c",
                        "src/misc/unix/rand.c",
                        "src/misc/unix/randbyte_os2.inc",
                        "src/misc/unix/charset.c",
                        "src/misc/unix/getopt.c",
                        "src/misc/unix/env.c",
                        "src/misc/unix/version.c",
                        "src/locks/unix",
                        "src/locks/unix/thread_mutex.c",
                        "src/locks/unix/proc_mutex.c",
                        "src/locks/unix/global_mutex.c",
                        "src/locks/unix/thread_cond.c",
                        "src/locks/unix/thread_rwlock.c",
                        "src/memory/unix",
                        "src/memory/unix/apr_pools.c",
                        "src/network_io/unix",
                        "src/network_io/unix/sockets.c",
                        "src/network_io/unix/multicast.c",
                        "src/network_io/unix/sendrecv.c",
                        "src/network_io/unix/socket_util.c",
                        "src/network_io/unix/inet_ntop.c",
                        "src/network_io/unix/sockopt.c",
                        "src/network_io/unix/sockaddr.c",
                        "src/network_io/unix/inet_pton.c",
                        "src/atomic/unix",
                        "src/atomic/unix/mutex.c",
                        "src/atomic/unix/s390.c",
                        "src/atomic/unix/solaris.c",
                        "src/atomic/unix/builtins.c",
                        "src/atomic/unix/ia32.c",
                        "src/atomic/unix/ppc.c",
                        "src/poll/unix",
                        "src/poll/unix/poll.c",
                        "src/poll/unix/epoll.c",
                        "src/poll/unix/z_asio.c",
                        "src/poll/unix/pollset.c",
                        "src/poll/unix/pollcb.c",
                        "src/poll/unix/select.c",
                        "src/poll/unix/kqueue.c",
                        "src/poll/unix/wakeup.c",
                        "src/poll/unix/port.c",
                        "src/mmap/unix",
                        "src/mmap/unix/common.c",
                        "src/mmap/unix/mmap.c",
                        "src/support/unix",
                        "src/support/unix/waitio.c",
                        "src/dso/unix",
                        "src/dso/unix/dso.c",
                        "src/user/unix",
                        "src/user/unix/userinfo.c",
                        "src/user/unix/groupinfo.c",
                        "src/random/unix",
                        "src/random/unix/sha2.h",
                        "src/random/unix/apr_random.c",
                        "src/random/unix/sha2_glue.c",
                        "src/random/unix/sha2.c",
                        "src/file_io/unix",
                        "src/file_io/unix/tempdir.c",
                        "src/file_io/unix/pipe.c",
                        "src/file_io/unix/seek.c",
                        "src/file_io/unix/filedup.c",
                        "src/file_io/unix/buffer.c",
                        "src/file_io/unix/filepath_util.c",
                        "src/file_io/unix/open.c",
                        "src/file_io/unix/copy.c",
                        "src/file_io/unix/dir.c",
                        "src/file_io/unix/fileacc.c",
                        "src/file_io/unix/flock.c",
                        "src/file_io/unix/mktemp.c",
                        "src/file_io/unix/filepath.c",
                        "src/file_io/unix/fullrw.c",
                        "src/file_io/unix/filestat.c",
                        "src/file_io/unix/printf.c",
                        "src/file_io/unix/readwrite.c",
                        "src/threadproc/unix",
                        "src/threadproc/unix/procsup.c",
                        "src/threadproc/unix/threadpriv.c",
                        "src/threadproc/unix/proc.c",
                        "src/threadproc/unix/thread.c",
                        "src/threadproc/unix/signals.c",
                        "src/include/arch/unix",
                        "src/include/arch/unix/apr_arch_thread_cond.h",
                        "src/include/arch/unix/apr_arch_thread_mutex.h",
                        "src/include/arch/unix/apr_arch_networkio.h",
                        "src/include/arch/unix/apr_arch_dso.h",
                        "src/include/arch/unix/apr_arch_file_io.h",
                        "src/include/arch/unix/apr_arch_global_mutex.h",
                        "src/include/arch/unix/apr_arch_proc_mutex.h",
                        "src/include/arch/unix/apr_arch_inherit.h",
                        "src/include/arch/unix/apr_arch_thread_rwlock.h",
                        "src/include/arch/unix/apr_arch_shm.h",
                        "src/include/arch/unix/apr_arch_atomic.h",
                        "src/include/arch/unix/apr_arch_threadproc.h",
                        "src/include/arch/unix/apr_arch_misc.h",
                        "src/include/arch/unix/apr_arch_poll_private.h",
                        "src/include/arch/unix/apr_arch_internal_time.h",
                        "src/time/unix/timestr.c",
                        "src/time/unix/time.c",

                        "src/dbm/apr_dbm.c",
                        "src/misc/win32/utf8.c",


                    ],
                    'link_settings':{
                        'libraries':[
                            '-lpthread',
                            '-ldl',
                            '-luuid',
                            '-lcrypt',
                        ]
                    },
                }],
				['OS != "win"',{
					'sources':[
					],
					'link_settings':{
						'libraries':[

						],
					},
				}],
				['OS == "win"',{
                    'include_dirs':[
                        "src/include/arch/win32",
                    ],
                    'direct_dependent_settings': {
                        'include_dirs': [
                            "src/include/arch/unix",
                        ]
                    },
					'link_settings': {
						'libraries': [
							'ws2_32.lib',
                            'Advapi32.lib',
                            'kernel32.lib',
                            'mswsock.lib',
                            'ole32.lib',

                            'shell32.lib',
                            'rpcrt4.lib',
                            #'libexpat.lib',

                            #'nss3.lib',
                            #'nspr4.lib'
						]
					},
                    'sources':[
                        "src/atomic/win32/apr_atomic.c",
                        "src/dso/win32/dso.c",
                        "src/file_io/win32/buffer.c",
                        "src/file_io/win32/dir.c",
                        "src/file_io/win32/filedup.c",
                        "src/file_io/win32/filepath.c",
                        "src/file_io/win32/filestat.c",
                        "src/file_io/win32/filesys.c",
                        "src/file_io/win32/flock.c",
                        "src/file_io/win32/open.c",
                        "src/file_io/win32/pipe.c",
                        "src/file_io/win32/readwrite.c",
                        "src/file_io/win32/seek.c",
                        "src/locks/win32/proc_mutex.c",
                        "src/locks/win32/thread_cond.c",
                        "src/locks/win32/thread_mutex.c",
                        "src/locks/win32/thread_rwlock.c",
                        "src/misc/win32/charset.c",
                        "src/misc/win32/env.c",
                        "src/misc/win32/internal.c",
                        "src/misc/win32/misc.c",
                        "src/misc/win32/rand.c",
                        "src/misc/win32/start.c",
                        "src/misc/win32/utf8.c",
                        "src/mmap/win32/mmap.c",
                        "src/network_io/win32/sendrecv.c",
                        "src/network_io/win32/sockets.c",
                        "src/network_io/win32/sockopt.c",
                        "src/shmem/win32/shm.c",
                        "src/threadproc/win32/proc.c",
                        "src/threadproc/win32/signals.c",
                        "src/threadproc/win32/thread.c",
                        "src/threadproc/win32/threadpriv.c",
                        "src/time/win32/time.c",
                        "src/time/win32/timestr.c",
                        "src/user/win32/groupinfo.c",
                        "src/user/win32/userinfo.c",
                    ]
				}]
				
			],
            'sources':[

                "apr.gyp",
                "build_windows.bat",

                "src/apr-config.in",
                "src/apr.dsp",
                "src/apr.dsw",
                "src/apr.pc.in",

               


                "src/buckets/apr_brigade.c",
                "src/buckets/apr_buckets.c",
                "src/buckets/apr_buckets_alloc.c",
                "src/buckets/apr_buckets_eos.c",
                "src/buckets/apr_buckets_file.c",
                "src/buckets/apr_buckets_flush.c",
                "src/buckets/apr_buckets_heap.c",
                "src/buckets/apr_buckets_mmap.c",
                "src/buckets/apr_buckets_pipe.c",
                "src/buckets/apr_buckets_pool.c",
                "src/buckets/apr_buckets_refcount.c",
                "src/buckets/apr_buckets_simple.c",
                "src/buckets/apr_buckets_socket.c",
                "src/crypto/apr_crypto.c",
                "src/crypto/apr_md4.c",
                "src/crypto/apr_md5.c",
                "src/crypto/apr_passwd.c",
                "src/crypto/apr_sha1.c",
                "src/crypto/apr_siphash.c",
                "src/crypto/crypt_blowfish.c",
                "src/crypto/getuuid.c",
                "src/crypto/uuid.c",
                "src/dbd/apr_dbd.c",
                
                "src/dbm/apr_dbm_sdbm.c",
                "src/dbm/sdbm/sdbm.c",
                "src/dbm/sdbm/sdbm_hash.c",
                "src/dbm/sdbm/sdbm_lock.c",
                "src/dbm/sdbm/sdbm_pair.c",
                
                "src/encoding/apr_base64.c",
                "src/encoding/apr_escape.c",
                "src/file_io/unix/copy.c",
                "src/file_io/unix/fileacc.c",
                "src/file_io/unix/filepath_util.c",
                "src/file_io/unix/fullrw.c",
                "src/file_io/unix/mktemp.c",
                "src/file_io/unix/tempdir.c",
                
                "src/hooks/apr_hooks.c",
                
                "src/memcache/apr_memcache.c",
                "src/memory/unix/apr_pools.c",
                "src/misc/unix/errorcodes.c",
                "src/misc/unix/getopt.c",
                "src/misc/unix/otherchild.c",
                "src/misc/unix/version.c",
               
                "src/mmap/unix/common.c",
                
                "src/network_io/unix/inet_ntop.c",
                "src/network_io/unix/inet_pton.c",
                "src/network_io/unix/multicast.c",
                "src/network_io/unix/sockaddr.c",
                "src/network_io/unix/socket_util.c",
                
                "src/passwd/apr_getpass.c",
                "src/poll/unix/poll.c",
                "src/poll/unix/pollcb.c",
                "src/poll/unix/pollset.c",
                "src/poll/unix/select.c",
                "src/poll/unix/wakeup.c",
                "src/random/unix/apr_random.c",
                "src/random/unix/sha2.c",
                "src/random/unix/sha2_glue.c",
                "src/redis/apr_redis.c",
                
                "src/strings/apr_cpystrn.c",
                "src/strings/apr_cstr.c",
                "src/strings/apr_fnmatch.c",
                "src/strings/apr_snprintf.c",
                "src/strings/apr_strings.c",
                "src/strings/apr_strnatcmp.c",
                "src/strings/apr_strtok.c",
                "src/strmatch/apr_strmatch.c",
                "src/tables/apr_hash.c",
                "src/tables/apr_skiplist.c",
                "src/tables/apr_tables.c",
                
                "src/uri/apr_uri.c",
                
                "src/util-misc/apr_date.c",
                "src/util-misc/apr_queue.c",
                "src/util-misc/apr_reslist.c",
                "src/util-misc/apr_rmm.c",
                "src/util-misc/apr_thread_pool.c",
                "src/util-misc/apu_dso.c",
                "src/xlate/xlate.c",
                "src/xml/apr_xml.c",
                "src/xml/apr_xml_expat.c",
                "src/xml/apr_xml_libxml2.c",

                
            ]
        },
        {
            'target_name': 'abts',
            'type': 'executable',
            'dependencies': [
                'apr',
                'apr-test',
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/abts.c",
                "src/test/abts.h",
            ]
        },
       {
            'target_name': 'dbd',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/dbd.c",
            ]
        },
       {
            'target_name': 'echod',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/echod.c",
            ]
        },
         {
            'target_name': 'globalmutexchild',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/globalmutexchild.c",
            ]
        },
        
        {
            'target_name': 'testucs',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/internal/testucs.c",
            ]
        },
        
         {
            'target_name': 'occhild',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/occhild.c",
            ]
        },
        {
            'target_name': 'proc_child',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/proc_child.c",
            ]
        },
        {
            'target_name': 'readchild',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/readchild.c",
            ]
        },
        {
            'target_name': 'sendfile',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/sendfile.c",
            ]
        },
        {
            'target_name': 'sockchild',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/sockchild.c",
            ]
        },
        {
            'target_name': 'sockperf',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/sockperf.c",
            ]
        },
        {
            'target_name': 'testapp',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/testapp.c",
            ]
        },
        {
            'target_name': 'testlockperf',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/testlockperf.c",
            ]
        },
        {
            'target_name': 'testmutexscope',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/testmutexscope.c",
            ]
        },
        {
            'target_name': 'testshmconsumer',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/testshmconsumer.c",
            ]
        },
        {
            'target_name': 'testshmproducer',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/testshmproducer.c",
            ]
        },
        {
            'target_name': 'tryread',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/test/tryread.c",
            ]
        },
    
        {
            'target_name': 'gen_test_char',
            'type': 'executable',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[
                "src/tools/gen_test_char.c",
            ]
        },


        {
            'target_name': 'apr-test',
            'type': 'static_library',
            'dependencies': [
                'apr'
            ],
            'include_dirs':[
               
            ],
            "defines":[
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
                "defines":[
                ],
            },
            'sources':[


                "src/test/abts_tests.h",
                "src/test/data",
                "src/test/data/billion-laughs.xml",
                "src/test/data/file_datafile.txt",
                "src/test/data/mmap_datafile.txt",
                
                
                "src/test/Makefile.in",
                "src/test/Makefile.win",
                "src/test/mod_test.c",
                #"src/test/nw_misc.c",
                
                
                
                "src/test/README",
                
                
                
                "src/test/testall.dsw",
                
                "src/test/testargs.c",
                "src/test/testatomic.c",
                "src/test/testbase64.c",
                "src/test/testbuckets.c",
                "src/test/testcond.c",
                "src/test/testcrypto.c",
                "src/test/testdate.c",
                "src/test/testdbd.c",
                "src/test/testdbm.c",
                "src/test/testdir.c",
                "src/test/testdll.dsp",
                "src/test/testdso.c",
                "src/test/testdup.c",
                "src/test/testenv.c",
                "src/test/testescape.c",
                "src/test/testfile.c",
                "src/test/testfilecopy.c",
                "src/test/testfileinfo.c",
                "src/test/testflock.c",
                "src/test/testflock.h",
                "src/test/testfmt.c",
                "src/test/testfnmatch.c",
                "src/test/testglobalmutex.c",
                "src/test/testglobalmutex.h",
                "src/test/testhash.c",
                "src/test/testhooks.c",
                "src/test/testipsub.c",
                "src/test/testlfs.c",
                "src/test/testlfsabi.c",
                "src/test/testlfsabi.h",
                "src/test/testlfsabi32.c",
                "src/test/testlfsabi64.c",
                "src/test/testlfsabi_include.c",
                "src/test/testlib.dsp",
                "src/test/testlock.c",
                
                "src/test/testmd4.c",
                "src/test/testmd5.c",
                "src/test/testmemcache.c",
                "src/test/testmmap.c",
                
                "src/test/testnames.c",
                "src/test/testoc.c",
                "src/test/testpass.c",
                "src/test/testpath.c",
                "src/test/testpipe.c",
                "src/test/testpoll.c",
                "src/test/testpools.c",
                "src/test/testproc.c",
                "src/test/testprocmutex.c",
                "src/test/testqueue.c",
                "src/test/testrand.c",
                "src/test/testredis.c",
                "src/test/testreslist.c",
                "src/test/testrmm.c",
                "src/test/testshm.c",
                "src/test/testshm.h",
                
                
                "src/test/testsiphash.c",
                "src/test/testskiplist.c",
                "src/test/testsleep.c",
                "src/test/testsock.c",
                "src/test/testsock.h",
                "src/test/testsockets.c",
                "src/test/testsockopt.c",
                "src/test/teststr.c",
                "src/test/teststrmatch.c",
                "src/test/teststrnatcmp.c",
                "src/test/testtable.c",
                "src/test/testtemp.c",
                "src/test/testthread.c",
                "src/test/testtime.c",
                "src/test/testud.c",
                "src/test/testuri.c",
                "src/test/testuser.c",
                "src/test/testutil.c",
                "src/test/testutil.h",
                "src/test/testuuid.c",
                "src/test/testvsn.c",
                "src/test/testxlate.c",
                "src/test/testxml.c",
                

            ]
        },
        ],
        'conditions':[
            ['OS == "beos"',{
                'targets':[
                    {
                        'target_name': 'apr_proc_stub',
                        'type': 'executable',
                        'dependencies': [
                            'apr'
                        ],
                        'include_dirs':[
                        
                        ],
                        "defines":[
                        ],
                        'direct_dependent_settings': {
                            'include_dirs': [
                            ],
                            "defines":[
                            ],
                        },
                        'sources':[
                            "src/threadproc/beos/apr_proc_stub.c",
                        ]
                    },
                ]
            }],
            ['OS != "win"',{
                'targets':[
                    {
                        'target_name': 'jlibtool',
                        'type': 'executable',
                        'dependencies': [
                            'apr'
                        ],
                        'include_dirs':[
                        
                        ],
                        "defines":[
                        ],
                        'direct_dependent_settings': {
                            'include_dirs': [
                            ],
                            "defines":[
                            ],
                        },
                        'sources':[
                            "src/build/jlibtool.c",
                        ]
                    },
                    {
                        'target_name': 'testregex',
                        'type': 'executable',
                        'dependencies': [
                            'apr'
                        ],
                        'include_dirs':[
                        
                        ],
                        "defines":[
                        ],
                        'direct_dependent_settings': {
                            'include_dirs': [
                            ],
                            "defines":[
                            ],
                        },
                        'sources':[
                            "src/test/internal/testregex.c",
                        ]
                    },
                ]
            }]
    ]
}
