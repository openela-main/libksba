Summary: CMS and X.509 library
Name:    libksba
Version: 1.3.5
Release: 9%{?dist}

# The library is licensed under LGPLv3+ or GPLv2+,
# the rest of the package under GPLv3+
License: (LGPLv3+ or GPLv2+) and GPLv3+
Group:   System Environment/Libraries
URL:     http://www.gnupg.org/
Source0: ftp://ftp.gnupg.org/gcrypt/libksba/libksba-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/libksba/libksba-%{version}.tar.bz2.sig
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1: libksba-1.3.0-multilib.patch
# Fix for CVE-2022-3515
Patch2: libksba-1.5.1-overflow.patch

BuildRequires: gawk
BuildRequires: libgpg-error-devel >= 1.8
BuildRequires: libgcrypt-devel >= 1.2.0

%description
KSBA (pronounced Kasbah) is a library to make X.509 certificates as
well as the CMS easily accessible by other applications.  Both
specifications are building blocks of S/MIME and TLS.

%package devel
Summary: Development headers and libraries for %{name}
Group:   Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
%description devel
%{summary}.


%prep
%setup -q

%patch1 -p1 -b .multilib
%patch2 -p1 -b .overflow


%build
%configure \
  --disable-dependency-tracking \
  --disable-static

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


%check
make check


%ldconfig_scriptlets

%post devel
install-info %{_infodir}/ksba.info %{_infodir}/dir ||:

%preun devel
if [ $1 -eq 0 ]; then
  install-info --delete %{_infodir}/ksba.info %{_infodir}/dir ||:
fi


%files
%defattr(-,root,root,-)
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%{_libdir}/libksba.so.8*

%files devel
%defattr(-,root,root,-)
%{_bindir}/ksba-config
%{_libdir}/libksba.so
%{_includedir}/ksba.h
%{_datadir}/aclocal/ksba.m4
%{_infodir}/ksba.info*


%changelog
* Wed Jan 25 2023 Jakub Jelen <jjelen@redhat.com> - 1.3.5-9
- Fix for CVE-2022-47629 (#2161571)

* Wed Oct 19 2022 Jakub Jelen <jjelen@redhat.com> - 1.3.5-8
- Fix for CVE-2022-3515 (#2135702)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.5-6
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  2 2017 Tomáš Mráz <tmraz@redhat.com> - 1.3.5-2
- mark license files as such in the file list (#1418513)

* Mon Aug 29 2016 Tomáš Mráz <tmraz@redhat.com> - 1.3.5-1
- new upstream release fixing minor security issues

* Thu May 12 2016 Tomáš Mráz <tmraz@redhat.com> - 1.3.4-1
- new upstream release fixing minor security issues

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Tomáš Mráz <tmraz@redhat.com> - 1.3.3-1
- new upstream release fixing minor security issues

* Wed Nov 26 2014 Tomáš Mráz <tmraz@redhat.com> - 1.3.2-1
- new upstream release fixing a security issue

* Fri Sep 19 2014 Tomáš Mráz <tmraz@redhat.com> - 1.3.1-1
- new upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec  3 2012 Tomas Mraz <tmraz@redhat.com> - 1.3.0-2
- fix multilib conflict in libksba-config

* Wed Nov 21 2012 Tomas Mraz <tmraz@redhat.com> - 1.3.0-1
- new upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Tomas Mraz <tmraz@redhat.com> - 1.2.0-1
- new upstream version

* Thu Jun 02 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.8-3
- libksba-devel multilib conflict (#601976)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.8-1
- libksba-1.0.8

* Fri Jan  8 2010 Tomas Mraz <tmraz@redhat.com> - 1.0.7-1
- new upstream version

* Thu Dec 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.6-4
- better (upstreamable) multilib patch
- tighten %%files a bit

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0.6-3
- Convert specfile to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 20 2009 Rex Dieter <rdieter@fedorproject.org> - 1.0.6-1
- libksba-1.0.6
- -devel: fix info scriptlet

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 09 2009 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-1
- libksba-1.0.5

* Tue Sep 23 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.4-1
- libksba-1.0.4

* Thu Apr 03 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-2
- multiarch conflicts (#342201)

* Tue Feb 12 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-1
- libksba-1.0.3

* Fri Feb 08 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.2-4
- respin (gcc43)

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.2-3
- BR: gawk

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.2-2
- respin (ppc32, BuildID)
- License: GPLv3

* Fri Jul 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.2-1
- libksba-1.0.2

* Fri Dec 01 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.1-1
- libksba-1.0.1

* Mon Oct 02 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.0-1.1
- respin

* Thu Aug 31 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.0-1
- libksba-1.0.0

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.15-3
- fc6 respin

* Tue Jun 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.15-2
- 0.9.15

* Wed Mar 1 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.13-2.1
- fc5: gcc/glibc respin

* Wed Nov 30 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.13-2
- remove hacks
- drop self Obsoletes

* Wed Nov 30 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.13-1
- 0.9.13

* Fri Aug 26 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.11-3
- botched Obsoletes good, let's try again.

* Fri Aug 26 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.11-2
- revert to 0.9.11 (0.9.12 makes gnupg2 fail on x86_64) using Obsoletes
  to avoid Epoch or other ugly means.

* Mon Aug  8 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.12-1
- 0.9.12
- --disable-static

* Thu Apr 21 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.11-1
- 0.9.11
- drop upstreamed acquote patch

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.9-2
- rebuilt

* Tue Feb  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.9.9-1
- Minus BR libtool, add epoch to -devel req, fix underquoted ksba.m4.

* Fri Oct 22 2004 Rex Dieter <rexdieter[AT]users.sf.net> 0:0.9.9-0.fdr.2
- remove hard-coded .gz from %%post/%%postun
- add %%check section

* Tue Oct 19 2004 Rex Dieter <rexdieter[AT]users.sf.net> 0:0.9.9-0.fdr.1
- 0.9.9

* Thu Mar 20 2003 Ville Skyttä <ville.skytta@iki.fi> - 0.4.7-0.fdr.1
- Update to 0.4.7, and to current Fedora guidelines.
- Exclude %%{_libdir}/*.la.

* Wed Feb 12 2003 Warren Togami <warren@togami.com> 0.4.6-1.fedora.3
- temporary workaround to lib/dir conflict problem

* Sat Feb  8 2003 Ville Skyttä <ville.skytta@iki.fi> - 0.4.6-1.fedora.1
- First Fedora release.
