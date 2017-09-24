{
    'variables': {
        #'library': 'static_library',
        'library' : 'shared_library',
    },
    #gen_test_char!!!
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
                "src/include/arch/win32",
                "src/include/arch/unix",
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
                    "src/include/arch/win32",
                    "src/include/arch/unix",
                    "config",
                    "config/<(OS)",
                    "config/<(OS)/<(target_arch)",
                ],
                "defines":[
                ],
            },
            'conditions':[
				['OS != "win"',{
					'sources':[
					],
					'link_settings':{
						'libraries':[
						],
					},
				}],
				['OS == "win"',{
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
					}
				}]
				
			],
            'sources':[

                "apr.gyp",
                "build_windows.bat",

                "src/apr-config.in",
                "src/apr.dsp",
                "src/apr.dsw",
                "src/apr.pc.in",

                "src/atomic/win32/apr_atomic.c",
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
                #"src/dbm/apr_dbm.c",
                "src/dbm/apr_dbm_sdbm.c",
                "src/dbm/sdbm/sdbm.c",
                "src/dbm/sdbm/sdbm_hash.c",
                "src/dbm/sdbm/sdbm_lock.c",
                "src/dbm/sdbm/sdbm_pair.c",
                "src/dso/win32/dso.c",
                "src/encoding/apr_base64.c",
                "src/encoding/apr_escape.c",
                "src/file_io/unix/copy.c",
                "src/file_io/unix/fileacc.c",
                "src/file_io/unix/filepath_util.c",
                "src/file_io/unix/fullrw.c",
                "src/file_io/unix/mktemp.c",
                "src/file_io/unix/tempdir.c",
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
                "src/hooks/apr_hooks.c",
                "src/locks/win32/proc_mutex.c",
                "src/locks/win32/thread_cond.c",
                "src/locks/win32/thread_mutex.c",
                "src/locks/win32/thread_rwlock.c",
                "src/memcache/apr_memcache.c",
                "src/memory/unix/apr_pools.c",
                "src/misc/unix/errorcodes.c",
                "src/misc/unix/getopt.c",
                "src/misc/unix/otherchild.c",
                "src/misc/unix/version.c",
                "src/misc/win32/charset.c",
                "src/misc/win32/env.c",
                "src/misc/win32/internal.c",
                "src/misc/win32/misc.c",
                "src/misc/win32/rand.c",
                "src/misc/win32/start.c",
                "src/misc/win32/utf8.c",
                "src/mmap/unix/common.c",
                "src/mmap/win32/mmap.c",
                "src/network_io/unix/inet_ntop.c",
                "src/network_io/unix/inet_pton.c",
                "src/network_io/unix/multicast.c",
                "src/network_io/unix/sockaddr.c",
                "src/network_io/unix/socket_util.c",
                "src/network_io/win32/sendrecv.c",
                "src/network_io/win32/sockets.c",
                "src/network_io/win32/sockopt.c",
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
                "src/shmem/win32/shm.c",
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
                "src/threadproc/win32/proc.c",
                "src/threadproc/win32/signals.c",
                "src/threadproc/win32/thread.c",
                "src/threadproc/win32/threadpriv.c",
                "src/time/win32/time.c",
                "src/time/win32/timestr.c",
                "src/uri/apr_uri.c",
                "src/user/win32/groupinfo.c",
                "src/user/win32/userinfo.c",
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

                
                

               # "src/buckets/apr_brigade.c",
               # "src/buckets/apr_buckets.c",
               # "src/buckets/apr_buckets_alloc.c",
               # "src/buckets/apr_buckets_eos.c",
               # "src/buckets/apr_buckets_file.c",
               # "src/buckets/apr_buckets_flush.c",
               # "src/buckets/apr_buckets_heap.c",
               # #"src/buckets/apr_buckets_mmap.c",
               # "src/buckets/apr_buckets_pipe.c",
               # "src/buckets/apr_buckets_pool.c",
               # "src/buckets/apr_buckets_refcount.c",
               # "src/buckets/apr_buckets_simple.c",
               # "src/buckets/apr_buckets_socket.c",
#
               # "src/build/aprapp.dsp",
               # "src/build/aprconf.py",
               # "src/build/aprenv.py",
               # "src/build/apr_common.m4",
               # "src/build/apr_hints.m4",
               # "src/build/apr_network.m4",
               # "src/build/apr_rules.mk.in",
               # "src/build/apr_threads.m4",
               # "src/build/apr_win32.m4",
               # "src/build/apu-conf.m4",
               # "src/build/apu-hints.m4",
               # "src/build/buildcheck.sh",
               # "src/build/config.guess",
               # "src/build/config.sub",
               # "src/build/crypto.m4",
               # "src/build/cvtdsp.pl",
               # "src/build/dbd.m4",
               # "src/build/dbm.m4",
               # "src/build/dso.m4",
               # "src/build/find_apr.m4",
               # "src/build/fixwin32mak.pl",
               # "src/build/gen-build.py",
               # "src/build/get-version.sh",
               # "src/build/iconv.m4",
               # "src/build/install.sh",
               # "src/build/libaprapp.dsp",
               # "src/build/lineends.pl",
               # "src/build/MakeEtags",
               # "src/build/make_exports.awk",
               # "src/build/make_nw_export.awk",
               # "src/build/make_var_export.awk",
               # "src/build/mkdir.sh",
               # "src/build/NWGNUenvironment.inc",
               # "src/build/NWGNUhead.inc",
               # "src/build/NWGNUmakefile",
               # "src/build/NWGNUtail.inc",
               # "src/build/nw_export.h",
               # "src/build/nw_ver.awk",
               # "src/build/pkg",
               # "src/build/pkg/buildpkg.sh",
               # "src/build/pkg/pkginfo.in",
               # "src/build/pkg/README",
               # "src/build/preaprapp.dsp",
               # "src/build/prelibaprapp.dsp",
               # "src/build/PrintPath",
               # "src/build/rpm",
               # "src/build/rpm/apr.spec.in",
               # "src/build/run-gcov.sh",
               # "src/build/subst.py",
               # "src/build/win32ver.awk",
               # "src/build/xml.m4",
               # "src/build/__init__.py",
               # "src/build.conf",
               # "src/buildconf",
               # "src/CHANGES",
               # "src/CMakeLists.txt",
               # "src/config.layout",
               # "src/configure.in",
#
               # "src/crypto/apr_crypto.c",
               # "src/crypto/apr_crypto_commoncrypto.c",
               # "src/crypto/apr_crypto_nss.c",
               # "src/crypto/apr_crypto_nss.dsp",
               # "src/crypto/apr_crypto_openssl.c",
               # "src/crypto/apr_crypto_openssl.dsp",
               # "src/crypto/apr_md4.c",
               # "src/crypto/apr_md5.c",
               # "src/crypto/apr_passwd.c",
               # "src/crypto/apr_sha1.c",
               # "src/crypto/apr_siphash.c",
               # "src/crypto/crypt_blowfish.c",
               # "src/crypto/crypt_blowfish.h",
               # "src/crypto/getuuid.c",
               # "src/crypto/uuid.c",
#
#
               # "src/dbd/apr_dbd.c",
               # "src/dbd/apr_dbd_mysql.c",
               # "src/dbd/apr_dbd_mysql.dsp",
               # "src/dbd/apr_dbd_odbc.c",
               # "src/dbd/apr_dbd_odbc.dsp",
               # "src/dbd/apr_dbd_oracle.c",
               # "src/dbd/apr_dbd_oracle.dsp",
               # "src/dbd/apr_dbd_pgsql.c",
               # "src/dbd/apr_dbd_pgsql.dsp",
               # "src/dbd/apr_dbd_sqlite2.c",
               # "src/dbd/apr_dbd_sqlite2.dsp",
               # "src/dbd/apr_dbd_sqlite3.c",
               # "src/dbd/apr_dbd_sqlite3.dsp",
#
#
               # "src/dbd/unsupported/apr_dbd_freetds.c",
               # "src/dbd/unsupported/apr_dbd_freetds.dsp",
#
#
               # #"src/dbm/apr_dbm.c",
               #"src/dbm/apr_dbm_berkeleydb.c",
               # "src/dbm/apr_dbm_db.dsp",
               # "src/dbm/apr_dbm_gdbm.c",
               # "src/dbm/apr_dbm_gdbm.dsp",
               # "src/dbm/apr_dbm_ndbm.c",
               # "src/dbm/apr_dbm_sdbm.c",
#
               # "src/dbm/sdbm/sdbm.c",
               # "src/dbm/sdbm/sdbm_hash.c",
               # "src/dbm/sdbm/sdbm_lock.c",
               # "src/dbm/sdbm/sdbm_pair.c",
               # "src/dbm/sdbm/sdbm_pair.h",
               # "src/dbm/sdbm/sdbm_private.h",
               # "src/dbm/sdbm/sdbm_tune.h",
#
#
#
#
#
               # #"src/include/arch/os390/apr_arch_dso.h",
               # #"src/atomic/os390/atomic.c",
               # #"src/dso/os390/dso.c",
#
#
#
               # "src/encoding/apr_base64.c",
               # #"src/encoding/apr_escape.c",
#
#
#
#
               # "src/hooks/apr_hooks.c",
#
               # "src/include/apr.h.in",
               # "src/include/apr.hnw",
               # "src/include/apr.hw",
               # "src/include/apr.hwc",
               # "src/include/apr_allocator.h",
               # "src/include/apr_anylock.h",
               # "src/include/apr_atomic.h",
               # "src/include/apr_base64.h",
               # "src/include/apr_buckets.h",
               # "src/include/apr_crypto.h",
               # "src/include/apr_cstr.h",
               # "src/include/apr_date.h",
               # "src/include/apr_dbd.h",
               # "src/include/apr_dbm.h",
               # "src/include/apr_dso.h",
               # "src/include/apr_env.h",
               # "src/include/apr_errno.h",
               # "src/include/apr_escape.h",
               # "src/include/apr_file_info.h",
               # "src/include/apr_file_io.h",
               # "src/include/apr_fnmatch.h",
               # "src/include/apr_general.h",
               # "src/include/apr_getopt.h",
               # "src/include/apr_global_mutex.h",
               # "src/include/apr_hash.h",
               # "src/include/apr_hooks.h",
               # "src/include/apr_inherit.h",
               # "src/include/apr_lib.h",
               # "src/include/apr_md4.h",
               # "src/include/apr_md5.h",
               # "src/include/apr_memcache.h",
               # "src/include/apr_mmap.h",
               # "src/include/apr_network_io.h",
               # "src/include/apr_optional.h",
               # "src/include/apr_optional_hooks.h",
               # "src/include/apr_perms_set.h",
               # "src/include/apr_poll.h",
               # "src/include/apr_pools.h",
               # "src/include/apr_portable.h",
               # "src/include/apr_proc_mutex.h",
               # "src/include/apr_queue.h",
               # "src/include/apr_random.h",
               # "src/include/apr_redis.h",
               # "src/include/apr_reslist.h",
               # "src/include/apr_ring.h",
               # "src/include/apr_rmm.h",
               # "src/include/apr_sdbm.h",
               # "src/include/apr_sha1.h",
               # "src/include/apr_shm.h",
               # "src/include/apr_signal.h",
               # "src/include/apr_siphash.h",
               # "src/include/apr_skiplist.h",
               # "src/include/apr_strings.h",
               # "src/include/apr_strmatch.h",
               # "src/include/apr_tables.h",
               # "src/include/apr_thread_cond.h",
               # "src/include/apr_thread_mutex.h",
               # "src/include/apr_thread_pool.h",
               # "src/include/apr_thread_proc.h",
               # "src/include/apr_thread_rwlock.h",
               # "src/include/apr_time.h",
               # "src/include/apr_uri.h",
               # "src/include/apr_user.h",
               # "src/include/apr_uuid.h",
               # "src/include/apr_version.h",
               # "src/include/apr_want.h",
               # "src/include/apr_xlate.h",
               # "src/include/apr_xml.h",
               # "src/include/apu.h",
               # "src/include/apu_errno.h",
               # "src/include/apu_version.h",
               # "src/include/apu_want.h.in",
               # "src/include/apu_want.hnw",
               # "src/include/apu_want.hw",
#
               # #"src/dso/aix/dso.c",
               # #"src/include/arch/aix/apr_arch_dso.h",
#
               # #"src/dso/beos/dso.c",
               # #"src/include/arch/beos/apr_arch_dso.h",
               # #"src/include/arch/beos/apr_arch_proc_mutex.h",
               # #"src/include/arch/beos/apr_arch_threadproc.h",
               # #"src/include/arch/beos/apr_arch_thread_cond.h",
               # #"src/include/arch/beos/apr_arch_thread_mutex.h",
               # #"src/include/arch/beos/apr_arch_thread_rwlock.h",
               # #"src/locks/beos/proc_mutex.c",
               # #"src/locks/beos/thread_cond.c",
               # #"src/locks/beos/thread_mutex.c",
               # #"src/locks/beos/thread_rwlock.c",
               # #"src/shmem/beos/shm.c",
               # #"src/network_io/beos/sendrecv.c",
               # #"src/network_io/beos/socketcommon.c",
               
               # #"src/threadproc/beos/proc.c",
               # #"src/threadproc/beos/thread.c",
               # #"src/threadproc/beos/threadpriv.c",
               # #"src/threadproc/beos/threadproc_common.c",
#
#
#
               # 
#
#
               # "src/include/private/apr_crypto_internal.h",
               # "src/include/private/apr_dbd_internal.h",
               # "src/include/private/apr_dbd_odbc_v2.h",
               # "src/include/private/apr_dbm_private.h",
               # "src/include/private/apr_support.h",
               # "src/include/private/apu_internal.h",
               # "src/include/private/apu_select_dbm.h.in",
               # "src/include/private/apu_select_dbm.hw",
               # "src/libapr.dsp",
               # "src/libapr.rc",
               # "src/LICENSE",
#
#
               # "src/memory/unix/apr_pools.c",
#
#
               # #"src/memcache/apr_memcache.c",
#
               # #"src/build/aplibtool.c",
               
#
               # #"src/dso/unix/dso.c",
               # #"src/atomic/unix/builtins.c",
               # #"src/atomic/unix/ia32.c",
               # #"src/atomic/unix/mutex.c",
               # #"src/atomic/unix/ppc.c",
               # #"src/atomic/unix/s390.c",
               # #"src/atomic/unix/solaris.c",
               # #"src/file_io/unix/buffer.c",
               # #"src/file_io/unix/copy.c",
               # #"src/file_io/unix/dir.c",
               # #"src/file_io/unix/fileacc.c",
               # #"src/file_io/unix/filedup.c",
               # #"src/file_io/unix/filepath.c",
               # #"src/file_io/unix/filepath_util.c",
               # #"src/file_io/unix/filestat.c",
               # #"src/file_io/unix/flock.c",
               # #"src/file_io/unix/fullrw.c",
               # #"src/file_io/unix/mktemp.c",
               # #"src/file_io/unix/open.c",
               # #"src/file_io/unix/pipe.c",
               # #"src/file_io/unix/printf.c",
               # #"src/file_io/unix/readwrite.c",
               # #"src/file_io/unix/seek.c",
               # #"src/file_io/unix/tempdir.c",
               # #"src/include/arch/unix/apr_arch_atomic.h",
               # #"src/include/arch/unix/apr_arch_dso.h",
               # #"src/include/arch/unix/apr_arch_file_io.h",
               # #"src/include/arch/unix/apr_arch_global_mutex.h",
               # #"src/include/arch/unix/apr_arch_inherit.h",
               # #"src/include/arch/unix/apr_arch_internal_time.h",
               # #"src/include/arch/unix/apr_arch_misc.h",
               # #"src/include/arch/unix/apr_arch_networkio.h",
               # #"src/include/arch/unix/apr_arch_poll_private.h",
               # #"src/include/arch/unix/apr_arch_proc_mutex.h",
               # #"src/include/arch/unix/apr_arch_shm.h",
               # #"src/include/arch/unix/apr_arch_threadproc.h",
               # #"src/include/arch/unix/apr_arch_thread_cond.h",
               # #"src/include/arch/unix/apr_arch_thread_mutex.h",
               # #"src/include/arch/unix/apr_arch_thread_rwlock.h",
               # #"src/locks/unix/global_mutex.c",
               # #"src/locks/unix/proc_mutex.c",
               # #"src/locks/unix/thread_cond.c",
               # #"src/locks/unix/thread_mutex.c",
               # #"src/locks/unix/thread_rwlock.c",
               # 
               # #"src/misc/unix/charset.c",
               # #"src/misc/unix/env.c",
               # #"src/misc/unix/errorcodes.c",
               # #"src/misc/unix/getopt.c",
               # #"src/misc/unix/otherchild.c",
               # #"src/misc/unix/rand.c",
               # #"src/misc/unix/randbyte_os2.inc",
               # #"src/misc/unix/start.c",
               # #"src/misc/unix/version.c",
               # #"src/mmap/unix/common.c",
               # #"src/mmap/unix/mmap.c",
               # #"src/network_io/unix/inet_ntop.c",
               # #"src/network_io/unix/inet_pton.c",
               # #"src/network_io/unix/multicast.c",
               # #"src/network_io/unix/sendrecv.c",
               # #"src/network_io/unix/sockaddr.c",
               # #"src/network_io/unix/sockets.c",
               # #"src/network_io/unix/socket_util.c",
               # #"src/network_io/unix/sockopt.c",
               # #"src/poll/unix/epoll.c",
               # #"src/poll/unix/kqueue.c",
               # #"src/poll/unix/poll.c",
               # #"src/poll/unix/pollcb.c",
               # #"src/poll/unix/pollset.c",
               # #"src/poll/unix/port.c",
               # #"src/poll/unix/select.c",
               # #"src/poll/unix/wakeup.c",
               # #"src/poll/unix/z_asio.c",
               # #"src/random/unix/apr_random.c",
               # #"src/random/unix/sha2.c",
               # #"src/random/unix/sha2.h",
               # #"src/random/unix/sha2_glue.c",
               # #"src/shmem/unix/shm.c",
               # #"src/support/unix/waitio.c",
               # #"src/threadproc/unix/proc.c",
               # #"src/threadproc/unix/procsup.c",
               # #"src/threadproc/unix/signals.c",
               # #"src/threadproc/unix/thread.c",
               # #"src/threadproc/unix/threadpriv.c",
               # #"src/time/unix/time.c",
               # #"src/time/unix/timestr.c",
               # #"src/user/unix/groupinfo.c",
               # #"src/user/unix/userinfo.c",
#
               # "src/atomic/win32/apr_atomic.c",
               # #"src/dso/win32/dso.c",
               # "src/file_io/win32/buffer.c",
               # "src/file_io/win32/dir.c",
               # "src/file_io/win32/filedup.c",
               # "src/file_io/win32/filepath.c",
               # "src/file_io/win32/filestat.c",
               # "src/file_io/win32/filesys.c",
               # "src/file_io/win32/flock.c",
               # "src/file_io/win32/open.c",
               # #"src/file_io/win32/pipe.c",
               # "src/file_io/win32/readwrite.c",
               # "src/file_io/win32/seek.c",
               # "src/include/arch/win32/apr_arch_atime.h",
               # "src/include/arch/win32/apr_arch_dso.h",
               # "src/include/arch/win32/apr_arch_file_io.h",
               # "src/include/arch/win32/apr_arch_inherit.h",
               # "src/include/arch/win32/apr_arch_misc.h",
               # "src/include/arch/win32/apr_arch_networkio.h",
               # "src/include/arch/win32/apr_arch_proc_mutex.h",
               # "src/include/arch/win32/apr_arch_threadproc.h",
               # "src/include/arch/win32/apr_arch_thread_cond.h",
               # "src/include/arch/win32/apr_arch_thread_mutex.h",
               # "src/include/arch/win32/apr_arch_thread_rwlock.h",
               # "src/include/arch/win32/apr_arch_utf8.h",
               # "src/include/arch/win32/apr_dbg_win32_handles.h",
               # "src/include/arch/win32/apr_private.h",
               # "src/locks/win32/proc_mutex.c",
               # "src/locks/win32/thread_cond.c",
               # "src/locks/win32/thread_mutex.c",
               # "src/locks/win32/thread_rwlock.c",
               # "src/misc/win32/apr_app.c",
               # "src/misc/win32/charset.c",
               # "src/misc/win32/env.c",
               # "src/misc/win32/internal.c",
               # "src/misc/win32/misc.c",
               # #"src/misc/win32/rand.c",
               # #"src/misc/win32/start.c",
               # "src/misc/win32/utf8.c",
               # "src/mmap/win32/mmap.c",
               # #"src/network_io/win32/sendrecv.c",
               # #"src/network_io/win32/sockets.c",
               # "src/network_io/win32/sockopt.c",
               # "src/shmem/win32/shm.c",
               # "src/threadproc/win32/proc.c",
               # "src/threadproc/win32/signals.c",
               # "src/threadproc/win32/thread.c",
               # "src/threadproc/win32/threadpriv.c",
               # "src/time/win32/time.c",
               # "src/time/win32/timestr.c",
               # "src/user/win32/groupinfo.c",
               # "src/user/win32/userinfo.c",
#
#
#
               # #"src/file_io/os2/buffer.c",
               # #"src/file_io/os2/copy.c",
               # #"src/file_io/os2/dir.c",
               # #"src/file_io/os2/dir_make_recurse.c",
               # #"src/file_io/os2/fileacc.c",
               # #"src/file_io/os2/filedup.c",
               # #"src/file_io/os2/filepath.c",
               # #"src/file_io/os2/filepath_util.c",
               # #"src/file_io/os2/filestat.c",
               # #"src/file_io/os2/filesys.c",
               # #"src/file_io/os2/flock.c",
               # #"src/file_io/os2/fullrw.c",
               # #"src/file_io/os2/link.c",
               # #"src/file_io/os2/maperrorcode.c",
               # #"src/file_io/os2/mktemp.c",
               # #"src/file_io/os2/open.c",
               # #"src/file_io/os2/pipe.c",
               # #"src/file_io/os2/printf.c",
               # #"src/file_io/os2/readwrite.c",
               # #"src/file_io/os2/seek.c",
               # #"src/file_io/os2/tempdir.c",
               # #"src/dso/os2/dso.c",
               # #"src/include/arch/os2/apr_arch_dso.h",
               # #"src/include/arch/os2/apr_arch_file_io.h",
               # #"src/include/arch/os2/apr_arch_networkio.h",
               # #"src/include/arch/os2/apr_arch_os2calls.h",
               # #"src/include/arch/os2/apr_arch_proc_mutex.h",
               # #"src/include/arch/os2/apr_arch_threadproc.h",
               # #"src/include/arch/os2/apr_arch_thread_cond.h",
               # #"src/include/arch/os2/apr_arch_thread_mutex.h",
               # #"src/include/arch/os2/apr_arch_thread_rwlock.h",
               # #"src/locks/os2/proc_mutex.c",
               # #"src/locks/os2/thread_cond.c",
               # #"src/locks/os2/thread_mutex.c",
               # #"src/locks/os2/thread_rwlock.c",
               # #"src/network_io/os2/inet_ntop.c",
               # #"src/network_io/os2/inet_pton.c",
               # #"src/network_io/os2/multicast.c",
               # #"src/network_io/os2/os2calls.c",
               # #"src/network_io/os2/sendrecv.c",
               # #"src/network_io/os2/sendrecv_udp.c",
               # #"src/network_io/os2/sockaddr.c",
               # #"src/network_io/os2/sockets.c",
               # #"src/network_io/os2/socket_util.c",
               # #"src/network_io/os2/sockopt.c",
               # #"src/poll/os2/poll.c",
               # #"src/poll/os2/pollcb.c",
               # #"src/poll/os2/pollset.c",
               # #"src/shmem/os2/shm.c",
               # #"src/support/os2/waitio.c",
               # #"src/threadproc/os2/proc.c",
               # #"src/threadproc/os2/signals.c",
               # #"src/threadproc/os2/thread.c",
               # #"src/threadproc/os2/threadpriv.c",
#
#
#
#
               # "src/passwd/apr_getpass.c",
#
#
#
               # "src/README",
#
#
               # #"src/redis/apr_redis.c",
#
#
#
#
               # "src/strings/apr_cpystrn.c",
               # "src/strings/apr_cstr.c",
               # "src/strings/apr_fnmatch.c",
               # #"src/strings/apr_snprintf.c",
               # "src/strings/apr_strings.c",
               # "src/strings/apr_strnatcmp.c",
               # "src/strings/apr_strtok.c",
#
               # "src/strmatch/apr_strmatch.c",
#
#
#
#
               # "src/tables/apr_hash.c",
               # "src/tables/apr_skiplist.c",
               # "src/tables/apr_tables.c",
#
#
#
#
               
#
               # "src/uri/apr_uri.c",
#
               # #"src/atomic/netware/apr_atomic.c",
               # #"src/dso/netware/dso.c",
               # #"src/file_io/netware/filestat.c",
               # #"src/file_io/netware/filesys.c",
               # #"src/file_io/netware/flock.c",
               # #"src/file_io/netware/mktemp.c",
               # #"src/file_io/netware/pipe.c",
               # #"src/include/arch/netware/apr_arch_dso.h",
               # #"src/include/arch/netware/apr_arch_file_io.h",
               # #"src/include/arch/netware/apr_arch_global_mutex.h",
               # #"src/include/arch/netware/apr_arch_internal_time.h",
               # #"src/include/arch/netware/apr_arch_networkio.h",
               # #"src/include/arch/netware/apr_arch_pre_nw.h",
               # #"src/include/arch/netware/apr_arch_proc_mutex.h",
               # #"src/include/arch/netware/apr_arch_threadproc.h",
               # #"src/include/arch/netware/apr_arch_thread_cond.h",
               # #"src/include/arch/netware/apr_arch_thread_mutex.h",
               # #"src/include/arch/netware/apr_arch_thread_rwlock.h",
               # #"src/include/arch/netware/apr_private.h",
               # #"src/locks/netware/proc_mutex.c",
               # #"src/locks/netware/thread_cond.c",
               # #"src/locks/netware/thread_mutex.c",
               # #"src/locks/netware/thread_rwlock.c",
               # #"src/misc/netware/apr.xdc",
               # #"src/misc/netware/charset.c",
               # #"src/misc/netware/libprews.c",
               # #"src/misc/netware/rand.c",
               # #"src/misc/netware/start.c",
               # #"src/threadproc/netware/proc.c",
               # #"src/threadproc/netware/procsup.c",
               # #"src/threadproc/netware/signals.c",
               # #"src/threadproc/netware/thread.c",
               # #"src/threadproc/netware/threadpriv.c",
               # #"src/user/netware/groupinfo.c",
               # #"src/user/netware/userinfo.c",
#
#
               # "src/util-misc/apr_date.c",
               # "src/util-misc/apr_queue.c",
               # "src/util-misc/apr_reslist.c",
               # "src/util-misc/apr_rmm.c",
               # "src/util-misc/apr_thread_pool.c",
               # "src/util-misc/apu_dso.c",
#
               # "src/xlate/xlate.c",
#
               # #"src/xml/apr_xml.c",
               # #"src/xml/apr_xml_expat.c",
               # #"src/xml/apr_xml_internal.h",
               # #"src/xml/apr_xml_libxml2.c",


            ]
        },
        {
            'target_name': 'abts',
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


                "src/test/abts_tests.h",
                "src/test/data",
                "src/test/data/billion-laughs.xml",
                "src/test/data/file_datafile.txt",
                "src/test/data/mmap_datafile.txt",
                
                
                "src/test/Makefile.in",
                "src/test/Makefile.win",
                "src/test/mod_test.c",
                "src/test/nw_misc.c",
                
                
                
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
        }
    ]
}
