%define upstream_name	 SVN-Notify-Mirror
%define upstream_version 0.038

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Keep a mirrored working copy of a repository path
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SVN/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(SVN::Notify)
BuildRequires:  subversion-tools
BuildRequires:  sendmail-command
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Keep a local directory in sync with a portion of a Subversion repository.
Typically used to keep a development web server in sync with the changes made
to the repository.

NOTE: because 'svn export' is not able to be consistently updated, the sync'd
directory must be a full working copy.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor << EOF
y
EOF
./Build

%check
export SVNLOOK=%{_bindir}/svnlook
export LC_ALL=C
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/SVN
%{_mandir}/*/*



